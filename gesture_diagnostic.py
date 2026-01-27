"""
GESTURE DETECTION DIAGNOSTIC TOOL
Shows exactly what gestures are being detected in real-time
Helps debug why gestures might not work
"""

import cv2
import sys
import time
from hand_control import HandGestureDetector
from face_control import HeadTiltDetector


def run_gesture_diagnostic():
    """Run gesture detection diagnostic."""
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ Cannot open camera!")
        return
    
    # Set camera properties
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)
    
    hand_detector = HandGestureDetector()
    face_detector = HeadTiltDetector()
    
    print("\n" + "="*70)
    print("🎮 GESTURE DETECTION DIAGNOSTIC")
    print("="*70)
    print("\nINSTRUCTIONS:")
    print("  1. Show your HAND in the camera frame")
    print("  2. Watch the left panel for gesture detection")
    print("  3. Check the printed output below for detected gesture")
    print("\nGESTURES TO TEST:")
    print("  ✋  PALM: Open hand, fingers spread wide")
    print("  ✊  FIST: Closed fist")
    print("  ✌️  REVERSE: Two fingers (peace sign)")
    print("\nPRESS: 'q' or 'ESC' to exit")
    print("="*70 + "\n")
    
    gesture_counts = {"PALM": 0, "FIST": 0, "REVERSE": 0, "NONE": 0}
    last_gesture = "NONE"
    gesture_change_time = time.time()
    
    frame_count = 0
    fps_time = time.time()
    fps = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to read frame")
            break
        
        frame_count += 1
        current_time = time.time()
        if current_time - fps_time >= 1:
            fps = frame_count
            frame_count = 0
            fps_time = current_time
        
        # Detect hand gesture
        frame, gesture = hand_detector.detect_gesture(frame, draw=True)
        
        # Detect face
        frame, face_direction = face_detector.detect_tilt(frame, draw=True)
        
        # Show FPS
        cv2.putText(frame, f"FPS: {fps}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        
        # Show current gesture (big text)
        gesture_color = (0, 255, 0) if gesture != "NONE" else (200, 200, 200)
        cv2.putText(frame, f"DETECTED: {gesture}", (10, 60),
                   cv2.FONT_HERSHEY_SIMPLEX, 1.2, gesture_color, 3)
        
        # Show face direction
        cv2.putText(frame, f"FACE: {face_direction}", (10, 200),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        
        # Update gesture statistics
        if gesture != last_gesture:
            gesture_counts[gesture] += 1
            last_gesture = gesture
            gesture_change_time = current_time
        
        # Show statistics panel
        stats_y = 250
        cv2.putText(frame, "STATISTICS:", (10, stats_y),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 0), 2)
        for gesture_name in ["PALM", "FIST", "REVERSE", "NONE"]:
            count = gesture_counts[gesture_name]
            cv2.putText(frame, f"{gesture_name}: {count} times", (10, stats_y + 30 + gesture_counts.keys().__len__() * 0),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)
        
        cv2.imshow("🎮 Gesture Detection Diagnostic", frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:  # 27 = ESC
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    print("\n" + "="*70)
    print("📊 DIAGNOSTIC SUMMARY")
    print("="*70)
    print(f"Gestures detected {sum(gesture_counts.values())} times total:")
    for gesture_name, count in gesture_counts.items():
        print(f"  {gesture_name}: {count} times")
    print("="*70 + "\n")
    
    if gesture_counts["NONE"] > 0.8 * sum(gesture_counts.values()):
        print("⚠️  WARNING: Mostly no hand detected!")
        print("     • Make sure your hand is in the camera frame")
        print("     • Check lighting - hand should be well-lit")
        print("     • Try moving hand closer/further from camera")
    else:
        print("✅ Gesture detection is working!")


if __name__ == "__main__":
    run_gesture_diagnostic()
