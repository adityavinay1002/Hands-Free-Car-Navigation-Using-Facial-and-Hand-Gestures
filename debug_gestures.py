"""
DEBUGGING GUIDE - Why Gestures Aren't Working
Run this to diagnose the exact problem
"""

import cv2
import sys
from hand_control import HandGestureDetector
from face_control import HeadTiltDetector


def debug_hand_detection():
    """Debug hand detection step by step."""
    print("\n" + "="*70)
    print("🔧 HAND DETECTION DEBUGGING")
    print("="*70)
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ CRITICAL: Cannot open camera!")
        return
    
    print("✅ Camera opened")
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    detector = HandGestureDetector()
    
    print("\n📋 DEBUGGING CHECKLIST:")
    print("   1. Make sure your HAND is in the frame")
    print("   2. Keep hand steady for 2-3 seconds")
    print("   3. Watch for green contour around hand")
    print("   4. If no contour appears, lighting might be too dark\n")
    
    frame_count = 0
    hands_detected = False
    
    import time
    start = time.time()
    
    while time.time() - start < 10:  # Run for 10 seconds
        ret, frame = cap.read()
        if not ret:
            break
        
        h, w, _ = frame.shape
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Apply adaptive threshold (same as hand_control.py)
        blurred = cv2.GaussianBlur(gray, (15, 15), 0)
        thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY_INV, 11, 2)
        
        # Morphological operations
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        
        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        # Show debug info
        debug_frame = frame.copy()
        cv2.putText(debug_frame, f"Contours found: {len(contours)}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        if len(contours) > 0:
            hand = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(hand)
            
            cv2.putText(debug_frame, f"Largest contour area: {int(area)}", (10, 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            if area > 500:
                hands_detected = True
                cv2.putText(debug_frame, "✅ HAND DETECTED!", (10, 90),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                # Draw hand
                cv2.drawContours(debug_frame, [hand], 0, (0, 255, 0), 2)
                
                # Get gesture
                _, gesture = detector.detect_gesture(frame, draw=False)
                cv2.putText(debug_frame, f"Gesture: {gesture}", (10, 120),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
            else:
                cv2.putText(debug_frame, f"⚠️  Area too small: {int(area)} (need >500)", (10, 90),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 165, 255), 2)
        else:
            cv2.putText(debug_frame, "❌ NO CONTOURS - hand not visible!", (10, 90),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        # Show binary threshold
        thresh_display = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
        combined = cv2.hconcat([debug_frame, thresh_display])
        
        cv2.imshow("Hand Detection Debug (LEFT: RGB | RIGHT: Binary Threshold)", combined)
        
        if cv2.waitKey(1) & 0xFF in [ord('q'), 27]:
            break
        
        frame_count += 1
    
    cap.release()
    cv2.destroyAllWindows()
    
    print("\n" + "="*70)
    print("📊 RESULTS")
    print("="*70)
    if hands_detected:
        print("✅ HAND DETECTION WORKING!")
    else:
        print("❌ HAND DETECTION FAILED")
        print("\nTroubleshooting steps:")
        print("   1. Check camera is working (try opening in other app)")
        print("   2. Ensure good lighting - dark lighting breaks detection")
        print("   3. Show hand prominently in center of frame")
        print("   4. Make sure hand is close enough (within 30-50cm)")
        print("   5. Check hand isn't too small in frame")


def debug_gesture_classification():
    """Test if gestures are being classified correctly."""
    print("\n" + "="*70)
    print("🎯 GESTURE CLASSIFICATION DEBUG")
    print("="*70)
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Cannot open camera!")
        return
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    detector = HandGestureDetector()
    
    print("\nTest each gesture:")
    print("   1. Show PALM (open hand, fingers spread) - Hold 3 seconds")
    print("   2. Show FIST (closed hand) - Hold 3 seconds")
    print("   3. Show REVERSE (two fingers, peace sign) - Hold 3 seconds\n")
    
    tested_gestures = {}
    
    import time
    start = time.time()
    
    while time.time() - start < 15:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame, gesture = detector.detect_gesture(frame, draw=True)
        
        if gesture != "NONE":
            if gesture not in tested_gestures:
                tested_gestures[gesture] = time.time()
                print(f"   ✅ Detected: {gesture}")
        
        # Display instructions
        cv2.putText(frame, f"Current: {gesture}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0) if gesture != "NONE" else (100, 100, 100), 2)
        
        cv2.imshow("Gesture Classification Test", frame)
        
        if cv2.waitKey(1) & 0xFF in [ord('q'), 27]:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    print("\n" + "="*70)
    print("📊 GESTURE TEST RESULTS")
    print("="*70)
    if tested_gestures:
        print(f"Detected gestures: {list(tested_gestures.keys())}")
        for gesture in ["PALM", "FIST", "REVERSE"]:
            if gesture in tested_gestures:
                print(f"   ✅ {gesture}: Working")
            else:
                print(f"   ❌ {gesture}: Not detected")
    else:
        print("❌ No gestures detected!")


def debug_keyboard_output():
    """Check if keyboard commands are being sent."""
    print("\n" + "="*70)
    print("⌨️  KEYBOARD OUTPUT DEBUG")
    print("="*70)
    
    try:
        import pyautogui
        print("✅ PyAutoGUI imported successfully")
        print("✅ Keyboard control available\n")
        
        from main import KeyboardController
        KeyboardController.configure()
        
        print("Testing keyboard output:")
        print("   - If you have a text editor open, it should show keypresses\n")
        
        import time
        gestures = [("PALM", "w"), ("FIST", None), ("REVERSE", "s")]
        
        for gesture_name, expected_key in gestures:
            print(f"   Simulating {gesture_name}...", end=" ")
            if expected_key:
                KeyboardController.press_key(expected_key)
                time.sleep(0.1)
                KeyboardController.release_key(expected_key)
                print(f"✅ ({expected_key} sent)")
            else:
                KeyboardController.release_key("w")
                KeyboardController.release_key("s")
                print("✅ (keys released)")
            time.sleep(0.3)
        
        print("\n✅ Keyboard output working!")
        
    except Exception as e:
        print(f"❌ Keyboard error: {e}")


if __name__ == "__main__":
    print("\n🔍 GESTURE RECOGNITION DEBUGGING SUITE")
    print("Helps identify exactly why gestures aren't working\n")
    
    choice = input("Select test:\n"
                   "1) Hand Detection Debug\n"
                   "2) Gesture Classification\n"
                   "3) Keyboard Output\n"
                   "4) Run All Tests\n"
                   "Choice (1-4): ").strip()
    
    if choice == "1":
        debug_hand_detection()
    elif choice == "2":
        debug_gesture_classification()
    elif choice == "3":
        debug_keyboard_output()
    elif choice == "4":
        debug_hand_detection()
        input("\nPress Enter to continue to gesture classification...")
        debug_gesture_classification()
        input("\nPress Enter to continue to keyboard output test...")
        debug_keyboard_output()
    else:
        print("Invalid choice")
