# Technical Approach

## Overview

This document describes the technical approach used to implement the hand tracking POC using classical computer vision techniques.

## System Architecture

```
┌─────────────┐
│   Camera    │
│   Input     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Preprocessing│
│  - Blur     │
│  - HSV      │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│Skin Detection│
│  - inRange  │
│  - Morph    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Contour   │
│  Detection  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Centroid   │
│Calculation  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Distance   │
│Measurement  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    State    │
│Classification│
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Visual    │
│   Overlay   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Display   │
└─────────────┘
```

## Detailed Algorithm

### 1. Frame Capture
- Capture frame from webcam using OpenCV
- Resolution: 640x480 pixels
- Mirror frame horizontally for intuitive interaction

### 2. Preprocessing
```python
# Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(frame, (5, 5), 0)

# Convert to HSV color space
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
```

**Why HSV?**
- Separates color (Hue) from intensity (Value)
- More robust to lighting variations than RGB
- Easier to define color ranges for skin detection

### 3. Skin Color Detection
```python
# Define skin color range in HSV
lower_bound = [0, 20, 70]    # Hue, Saturation, Value
upper_bound = [20, 255, 255]

# Create binary mask
mask = cv2.inRange(hsv, lower_bound, upper_bound)
```

**Color Range Selection:**
- **Hue (0-20)**: Orange to red (typical skin tones)
- **Saturation (20-255)**: Exclude very desaturated colors
- **Value (70-255)**: Exclude very dark regions

### 4. Morphological Operations
```python
# Remove noise with closing (fill holes)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# Remove small objects with opening
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
```

**Purpose:**
- **Closing**: Fills small holes in detected regions
- **Opening**: Removes small noise blobs
- **Result**: Cleaner, more continuous hand regions

### 5. Contour Detection
```python
# Find all contours
contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, 
                           cv2.CHAIN_APPROX_SIMPLE)

# Select largest contour (assumed to be hand)
largest = max(contours, key=cv2.contourArea)
```

**Assumptions:**
- Largest skin-colored region is the hand (or face)
- Minimum area threshold filters out noise
- External contours only (no nested contours)

### 6. Centroid Calculation
```python
# Calculate image moments
M = cv2.moments(contour)

# Calculate centroid
cx = int(M["m10"] / M["m00"])
cy = int(M["m01"] / M["m00"])
```

**Moments:**
- M00: Area of the contour
- M10: First moment around x-axis
- M01: First moment around y-axis
- Centroid = center of mass of the region

### 7. Distance Calculation
```python
# Euclidean distance in pixel space
distance = abs(centroid_x - boundary_x)
```

**Distance Metric:**
- Horizontal distance only (relevant for vertical boundary)
- Measured in pixels
- Simple and computationally efficient

### 8. State Classification
```python
if distance > 100:
    state = 'SAFE'
elif distance > 50:
    state = 'WARNING'
else:
    state = 'DANGER'
```

**Threshold Selection:**
- Based on typical hand size (50-100 pixels)
- Provides adequate warning time
- Can be adjusted for different use cases

### 9. Visualization
```python
# Draw boundary line
cv2.line(frame, (x, 0), (x, height), RED, 3)

# Draw contour
cv2.drawContours(frame, [contour], -1, GREEN, 2)

# Draw state text
cv2.putText(frame, state, position, font, size, color)
```

## Performance Optimization

### Why 30+ FPS on CPU?

1. **Efficient Algorithms:**
   - Color space conversion: O(n) where n = pixels
   - Morphological ops: O(n × k) where k = kernel size
   - Contour detection: O(n)
   - Overall: Linear time complexity

2. **Small Resolution:**
   - 640×480 = 307,200 pixels
   - Modern CPUs process this easily

3. **Vectorized Operations:**
   - NumPy/OpenCV use SIMD instructions
   - Parallel processing at CPU level

4. **Minimal Processing:**
   - No deep learning inference
   - No complex transformations
   - Direct pixel operations

## Alternative Approaches Considered

### 1. Background Subtraction
```python
bg_subtractor = cv2.createBackgroundSubtractorMOG2()
fg_mask = bg_subtractor.apply(frame)
```
**Pros:** Better isolation of moving hand  
**Cons:** Requires stationary camera, initial learning period

### 2. Edge Detection
```python
edges = cv2.Canny(gray, 50, 150)
```
**Pros:** Detects hand outline  
**Cons:** Sensitive to noise, harder to find centroid

### 3. Template Matching
```python
result = cv2.matchTemplate(frame, hand_template, method)
```
**Pros:** Can detect specific hand poses  
**Cons:** Not rotation/scale invariant, needs template

### 4. Machine Learning
```python
# Using MediaPipe or custom CNN
hand_landmarks = detector.process(frame)
```
**Pros:** Much more accurate and robust  
**Cons:** Requires GPU, higher complexity, violates assignment constraints

## Why Classical CV Was Chosen

1. **Assignment Requirement:** Explicitly requested no MediaPipe/OpenPose
2. **Performance:** Achieves 30 FPS easily on CPU
3. **Simplicity:** Clear, understandable algorithm
4. **Real-time:** Low latency for safety applications
5. **Resource Efficient:** No GPU needed

## Code Complexity Analysis

| Component | Lines of Code | Complexity |
|-----------|---------------|------------|
| Preprocessing | ~20 | Low |
| Detection | ~30 | Low |
| State Logic | ~15 | Very Low |
| Visualization | ~60 | Medium |
| Main Loop | ~50 | Low |
| **Total** | **~175** | **Low** |

**Maintainability:** High - clear separation of concerns, well-documented

## Testing Strategy

### Unit Testing Approach
- Test each function independently
- Use sample frames for reproducibility
- Verify state transitions with known distances

### Integration Testing
- Test complete pipeline with video input
- Verify FPS meets requirements
- Check state changes during hand movement

### Edge Cases Handled
- No hand detected → Returns infinity distance
- Multiple skin regions → Selects largest
- Poor lighting → Adjusts thresholds if needed
- Camera disconnection → Graceful error handling

## Future Optimization Opportunities

1. **Adaptive Thresholds:** Auto-adjust based on ambient lighting
2. **Kalman Filtering:** Smooth hand position predictions
3. **Multi-threading:** Separate capture and processing threads
4. **GPU Acceleration:** Use OpenCV CUDA module
5. **ROI Processing:** Only process region where hand expected

## Conclusion

This classical CV approach successfully demonstrates the feasibility of real-time hand tracking for proximity detection. While it has limitations in complex environments, it provides a solid foundation and exceeds the performance requirements of the POC.