"""
Quick Gesture Detection Test
Tests if hand detection is working at all
"""

import cv2
import numpy as np
from hand_control import HandGestureDetector


def test_gesture_detection():
    """Quick test of gesture detection."""
    print("\n" + "="*70)
    print("🧪 GESTURE DETECTION TEST")
    print("="*70)
    print("\nTesting hand gesture detection...")
    
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("❌ ERROR: Cannot open camera!")
            print("   • Check if camera is connected")
            print("   • Check if another app is using the camera")
            return False
        
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_FPS, 30)
        
        detector = HandGestureDetector()
        
        print("✅ Camera opened successfully")
        print("\nCapturing frames for 5 seconds...")
        print("   Show your hand to the camera...\n")
        
        gestures_seen = set()
        frame_num = 0
        
        import time
        start_time = time.time()
        
        while time.time() - start_time < 5:
            ret, frame = cap.read()
            if not ret:
                print("❌ Failed to read frame")
                break
            
            frame, gesture = detector.detect_gesture(frame, draw=False)
            
            if gesture != "NONE":
                gestures_seen.add(gesture)
                print(f"   Frame {frame_num}: Detected '{gesture}' ✓")
            else:
                print(f"   Frame {frame_num}: No hand detected")
            
            frame_num += 1
        
        cap.release()
        
        print("\n" + "="*70)
        print("📊 TEST RESULTS")
        print("="*70)
        print(f"Frames analyzed: {frame_num}")
        print(f"Gestures detected: {gestures_seen if gestures_seen else 'NONE'}")
        
        if not gestures_seen:
            print("\n⚠️  NO GESTURES DETECTED!")
            print("\nTroubleshooting:")
            print("   1. Make sure your HAND is clearly visible in camera")
            print("   2. Check lighting - good lighting is important")
            print("   3. Try different distances from camera (30-50cm)")
            print("   4. Make sure hand is in front of your face/body")
            return False
        else:
            print("\n✅ GESTURE DETECTION IS WORKING!")
            print("   Detected gestures:", ", ".join(gestures_seen))
            return True
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_gesture_detection()
    exit(0 if success else 1)
