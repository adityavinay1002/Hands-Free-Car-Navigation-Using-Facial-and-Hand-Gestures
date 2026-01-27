
import cv2
import numpy as np
from hand_control import HandGestureDetector

def create_skin_color_image(shape="circle"):
    # Create black background
    img = np.zeros((400, 400, 3), dtype=np.uint8)
    
    # Skin color in BGR (Approximate)
    # HSV (10, 150, 200) -> BGR conversion
    # But let's just use a hardcoded BGR that works for H=10
    # B=100, G=150, R=200 -> slightly peach/orange
    color = (100, 150, 200) 
    
    center = (200, 200)
    
    if shape == "fist":
        # Draw a circle (Fist)
        cv2.circle(img, center, 60, color, -1)
        
    elif shape == "palm":
        # Draw a star-like shape (5 fingers)
        # Center circle
        cv2.circle(img, center, 50, color, -1)
        # 5 Ellipses for fingers
        for angle in range(0, 360, 72): # 5 fingers
            # Convert angle to radians
            rad = np.radians(angle - 90) # Start from top
            # Finger position
            fx = int(200 + 90 * np.cos(rad))
            fy = int(200 + 90 * np.sin(rad))
            # Draw finger
            cv2.line(img, center, (fx, fy), color, 30)
            
    elif shape == "reverse":
        # Draw a V-shape (2 fingers)
        cv2.circle(img, center, 50, color, -1)
        # Finger 1 (Left)
        cv2.line(img, center, (150, 100), color, 30)
        # Finger 2 (Right)
        cv2.line(img, center, (250, 100), color, 30)

    return img

def test_detector():
    detector = HandGestureDetector(gesture_smoothing=1)
    
    shapes = ["fist", "palm", "reverse"]
    expected = {"fist": "FIST", "palm": "PALM", "reverse": "REVERSE"}
    
    print("Testing HandGestureDetector with synthetic images...")
    
    all_passed = True
    
    for shape in shapes:
        img = create_skin_color_image(shape)
        
        # Run detection
        # Note: We need to give it a few frames to clear the 'None' history if smoothing was > 1
        # But here smoothing is 1.
        
        processed_img, gesture = detector.detect_gesture(img, draw=False)
        
        print(f"Shape: {shape.upper():<10} -> Detected: {gesture:<10} | Expected: {expected[shape]}")
        
        if gesture != expected[shape]:
            # For PALM, sometimes star shape might have not enough deep defects depending on how I drew it
            # The 'Palm' drawing above is very crude (lines merging).
            # But let's see.
            if shape == "palm" and gesture == "PALM":
                pass 
            elif shape == "fist" and gesture == "FIST":
                pass
            elif shape == "reverse" and gesture == "REVERSE":
                pass
            else:
               # Allow some flexibility for synthetic shapes failure if logic is sound
               # But purely for this test:
               if shape == "palm" and gesture != "PALM":
                   print("  (Note: Synthetic palm might not have perfect convexity defects)")
               all_passed = False
        
        with open("verification_result.txt", "a") as f:
            f.write(f"Shape: {shape} -> Detected: {gesture} | Expected: {expected[shape]}\n")

    print("\nTest completed.")
    with open("verification_result.txt", "a") as f:
        f.write("Test completed.\n")

if __name__ == "__main__":
    test_detector()
