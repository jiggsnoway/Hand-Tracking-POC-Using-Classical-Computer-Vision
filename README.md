# Hand Tracking POC 👋

A real-time hand tracking system using classical computer vision techniques to detect hand proximity to virtual boundaries and trigger safety warnings.

## 📋 Overview

This Proof of Concept (POC) demonstrates real-time hand/fingertip tracking using a camera feed to detect when a user's hand approaches a virtual object on screen. The system classifies interactions into three states (SAFE, WARNING, DANGER) and displays appropriate visual feedback.

**Developed as part of:** Machine Learning Internship Assignment  
**Company:** Arvyax Technologies  
**Submission Date:** December 2025

## ✨ Features

- ✅ Real-time hand tracking without pre-built pose detection APIs
- ✅ Distance-based state classification (SAFE/WARNING/DANGER)
- ✅ Visual feedback with color-coded warnings
- ✅ "DANGER DANGER" alert when hand crosses boundary
- ✅ High performance: 30+ FPS on CPU-only execution
- ✅ Uses classical computer vision techniques (no MediaPipe/OpenPose)

## 🎯 Objectives Met

- [x] Real-time hand position tracking via camera feed
- [x] Virtual boundary drawn on screen
- [x] Distance-based state logic
- [x] Clear on-screen warning system
- [x] Performance: 30 FPS (exceeds 8 FPS requirement)
- [x] Classical CV techniques (color segmentation, contours)

## 🛠️ Technical Approach

### Detection Method
- **Color Space:** HSV (Hue, Saturation, Value)
- **Technique:** Skin color segmentation
- **Tracking:** Contour detection and centroid calculation
- **Distance Metric:** Euclidean distance in pixel space

### State Classification Logic
```
SAFE    → Distance > 100 pixels from boundary
WARNING → Distance 50-100 pixels from boundary  
DANGER  → Distance < 50 pixels from boundary
```

### Pipeline
```
Camera Feed → Preprocessing → Skin Detection → 
Contour Extraction → Centroid Calculation → 
Distance Measurement → State Classification → 
Visual Overlay → Display
```

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- Webcam
- pip (Python package manager)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/jiggsnoway/hand_tracking.git
cd hand_tracking
```

2. **Create virtual environment** (recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Run the application
```bash
python hand_tracking.py
```

### Controls
- **'q'** - Quit the application
- The system will open two windows:
  - Main tracking window with state visualization
  - Debug window showing hand mask

### Testing the System
1. Position yourself in front of the camera
2. Move your hand horizontally toward the red vertical line
3. Observe state changes:
   - Far from line → **GREEN** (SAFE)
   - Approaching line → **ORANGE** (WARNING)
   - Near/crossing line → **RED** (DANGER) + "DANGER DANGER" text

## 📊 Performance Results

| Metric | Target | Achieved | Status |
|--------|--------|----------|--------|
| FPS | ≥8 | 30+ | ✅ Exceeded |
| Detection | Real-time | Yes | ✅ |
| State Accuracy | High | High | ✅ |
| CPU Usage | Efficient | Low | ✅ |

### Sample Output
```
Frame: 30  | FPS: 31.5 | State: SAFE    | Distance: 301px
Frame: 60  | FPS: 30.2 | State: WARNING | Distance: 52px
Frame: 90  | FPS: 30.2 | State: DANGER  | Distance: 20px
```

## 📁 Project Structure

```
hand-tracking-poc/
├── .gitignore              # Git ignore rules
├── README.md               # This file
├── requirements.txt        # Python dependencies
├── hand_tracking.py        # Main application code
├── config.py              # Configuration settings
├── docs/                  # Additional documentation
│   ├── APPROACH.md        # Detailed technical approach
│   └── LIMITATIONS.md     # Known limitations

```

## 🔧 Configuration

You can adjust detection parameters in `config.py` or directly in the code:

```python
# HSV skin color range
LOWER_SKIN = np.array([0, 20, 70], dtype=np.uint8)
UPPER_SKIN = np.array([20, 255, 255], dtype=np.uint8)

# Distance thresholds (pixels)
SAFE_DISTANCE = 100
WARNING_DISTANCE = 50
DANGER_DISTANCE = 50

# Boundary position
BOUNDARY_X = 320  # Center of 640px width
```

## ⚠️ Limitations

### Known Issues
1. **Skin Detection:** Detects all skin-colored regions (face, arms, hands)
2. **Lighting Sensitivity:** Performance varies with lighting conditions
3. **Single Object:** Tracks only the largest detected contour
4. **2D Distance:** Measures distance in pixel space, not true 3D depth

See [docs/LIMITATIONS.md](docs/LIMITATIONS.md) for detailed analysis and potential solutions.

## 🔮 Future Enhancements

- [ ] Implement background subtraction for better hand isolation
- [ ] Add Region-of-Interest (ROI) filtering
- [ ] Support for YCrCb color space (better lighting invariance)
- [ ] Multi-hand tracking capability
- [ ] Depth estimation using hand size
- [ ] ML-based hand segmentation for improved accuracy
- [ ] Audio alerts in addition to visual warnings
- [ ] Configuration GUI for threshold adjustment

## 🧪 Testing

### Optimal Conditions
- ✅ Good lighting (natural or bright artificial light)
- ✅ Plain, non-skin-colored background
- ✅ Camera positioned to capture hand clearly
- ✅ Hand as the largest skin-colored object in frame

### Testing Checklist
- [ ] Hand moves from left to right → States change correctly
- [ ] Hand approaches boundary → WARNING triggered
- [ ] Hand crosses boundary → DANGER displayed
- [ ] No hand in frame → Shows "No hand detected"
- [ ] FPS counter shows 20+ FPS consistently

## 📚 Documentation

- **Detailed Approach:** [docs/APPROACH.md](docs/APPROACH.md)
- **Limitations & Solutions:** [docs/LIMITATIONS.md](docs/LIMITATIONS.md)

## 🤝 Contributing

This is a POC for an internship assignment. Not accepting contributions at this time.

## 📄 License

This project is for educational and demonstration purposes.

## 👤 Author

**[Jigyashman Hazarika]**
- Email: jiggsnoway18@gmail.com
- GitHub: (https://github.com/jiggsnoway)
- LinkedIn: [Jigyashman Hazarika](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- Assignment provided by Arvyax Technologies
- Guidance from Shalabh Bhatnagar
- OpenCV community for excellent documentation

## 📞 Contact

For questions or feedback about this POC:
- Email: jiggsnoway18@gmail.com
- Assignment Context: Machine Learning Internship - Arvyax Technologies

---

**Note:** This is a Proof of Concept demonstrating feasibility. For production deployment, additional robustness, error handling, and testing would be required.

**Submission Deadline:** December 7, 2025