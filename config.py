"""
Configuration file for Hand Tracking POC
Adjust these parameters to tune detection behavior
"""

import numpy as np


class Config:
    """Configuration parameters for hand tracking system"""
    
    # ========================================
    # Camera Settings
    # ========================================
    CAMERA_WIDTH = 640
    CAMERA_HEIGHT = 480
    CAMERA_ID = 0  # Default webcam
    FPS_TARGET = 8  # Minimum target FPS
    
    # ========================================
    # Skin Color Detection (HSV)
    # ========================================
    LOWER_SKIN = np.array([0, 20, 70], dtype=np.uint8)
    UPPER_SKIN = np.array([20, 255, 255], dtype=np.uint8)
    
    # Alternative HSV ranges (uncomment to use)
    # For lighter skin tones:
    # LOWER_SKIN = np.array([0, 10, 60], dtype=np.uint8)
    # UPPER_SKIN = np.array([25, 255, 255], dtype=np.uint8)
    
    # For darker skin tones:
    # LOWER_SKIN = np.array([0, 30, 80], dtype=np.uint8)
    # UPPER_SKIN = np.array([20, 200, 255], dtype=np.uint8)
    
    # ========================================
    # YCrCb Color Space (Alternative)
    # ========================================
    USE_YCRCB = False  # Set to True to use YCrCb instead of HSV
    LOWER_SKIN_YCRCB = np.array([0, 133, 77], dtype=np.uint8)
    UPPER_SKIN_YCRCB = np.array([255, 173, 127], dtype=np.uint8)
    
    # ========================================
    # Virtual Boundary Settings
    # ========================================
    BOUNDARY_TYPE = "line"  # Options: "line", "box", "circle"
    BOUNDARY_X = 320  # X-coordinate for vertical line (center of 640px)
    BOUNDARY_COLOR = (0, 0, 255)  # Red in BGR
    BOUNDARY_THICKNESS = 3
    
    # ========================================
    # Distance Thresholds (pixels)
    # ========================================
    SAFE_DISTANCE = 100      # Distance > 100px = SAFE
    WARNING_DISTANCE = 50    # Distance 50-100px = WARNING  
    DANGER_DISTANCE = 50     # Distance < 50px = DANGER
    
    # ========================================
    # Visual Settings
    # ========================================
    STATE_COLORS = {
        'SAFE': (0, 255, 0),      # Green
        'WARNING': (0, 165, 255),  # Orange
        'DANGER': (0, 0, 255)      # Red
    }
    
    # Font settings
    FONT = 0  # cv2.FONT_HERSHEY_SIMPLEX
    FONT_SCALE_LARGE = 1.2
    FONT_SCALE_MEDIUM = 0.8
    FONT_SCALE_SMALL = 0.6
    FONT_THICKNESS_BOLD = 3
    FONT_THICKNESS_NORMAL = 2
    
    # ========================================
    # Morphological Operations
    # ========================================
    KERNEL_SIZE = 5
    MORPH_ITERATIONS = 2
    
    # ========================================
    # Detection Settings
    # ========================================
    MIN_CONTOUR_AREA = 1000  # Minimum area to consider as hand (pixels²)
    BLUR_KERNEL_SIZE = (5, 5)
    
    # ========================================
    # Performance Settings
    # ========================================
    FPS_BUFFER_SIZE = 30  # Number of frames to average for FPS calculation
    SHOW_DEBUG_WINDOW = True  # Show hand mask debug window
    PRINT_INTERVAL = 30  # Print stats every N frames
    
    # ========================================
    # Advanced Options
    # ========================================
    # Prefer lower screen regions (where hands typically are)
    PREFER_LOWER_SCREEN = False
    LOWER_SCREEN_THRESHOLD = 0.4  # Use lower 60% of frame
    
    # Mirror camera feed (more intuitive interaction)
    MIRROR_CAMERA = True


# Create singleton instance
config = Config()


def print_config():
    """Print current configuration"""
    print("=" * 50)
    print("HAND TRACKING POC - CONFIGURATION")
    print("=" * 50)
    print(f"Camera: {config.CAMERA_WIDTH}x{config.CAMERA_HEIGHT}")
    print(f"Target FPS: ≥{config.FPS_TARGET}")
    print(f"Color Space: {'YCrCb' if config.USE_YCRCB else 'HSV'}")
    print(f"Boundary Position: x={config.BOUNDARY_X}")
    print(f"\nDistance Thresholds:")
    print(f"  SAFE:    > {config.SAFE_DISTANCE}px")
    print(f"  WARNING: {config.DANGER_DISTANCE}-{config.SAFE_DISTANCE}px")
    print(f"  DANGER:  < {config.DANGER_DISTANCE}px")
    print("=" * 50)


if __name__ == "__main__":
    # Print configuration when run directly
    print_config()