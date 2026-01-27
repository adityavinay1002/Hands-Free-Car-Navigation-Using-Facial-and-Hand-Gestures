"""
Hand Gesture Recognition - MEDIAPIPE VERSION (Robust)
Uses Google MediaPipe for skeletal tracking.
"""

import cv2
import mediapipe as mp
import time

class HandGestureDetector:
    """Detects hand gestures reliably using MediaPipe Hands."""
    
    def __init__(self, gesture_smoothing=5):
        """Initialize MediaPipe Hands."""
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            model_complexity=0, # LITE model for speed
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils
        
        # Debouncing / Sticky Logic
        self.stability_threshold = gesture_smoothing
        self.stable_gesture = "NONE"
        self.pending_gesture = "NONE"
        self.pending_frames = 0
        
    def detect_gesture(self, image, draw=True):
        """
        Detect hand gesture using MediaPipe Skeletal Tracking.
        """
        # Convert to RGB for MediaPipe
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)
        
        raw_gesture = "NONE"
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Count fingers
                fingers = []
                
                # Thumb (Check x position relative to IP joint depending on hand side)
                # Ideally we check handedness, but for simplicity let's use x distance
                # Logic: Tip x < IP x (Right hand palm facing camera)
                # Let's use a simpler heuristic: Tip distance to pinky base vs IP distance
                # Actually, standard logic:
                if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
                    fingers.append(1) # Thumb open (assuming right hand)
                else:
                    fingers.append(0)
                    
                # 4 Fingers (Index to Pinky) - Check Tip Y < PIP Y
                # Landmarks: 8, 12, 16, 20 are tips. 6, 10, 14, 18 are PIPs.
                tips = [8, 12, 16, 20]
                pips = [6, 10, 14, 18]
                
                for tip, pip in zip(tips, pips):
                    if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                
                # Total fingers open
                up_fingers = fingers[1:].count(1)
                
                # Check thumb separately or just rely on 4 fingers
                # Gestures:
                
                if up_fingers == 4: # 4 fingers up (Index, Middle, Ring, Pinky)
                    raw_gesture = "PALM"
                elif up_fingers == 0: # 0 fingers up
                    raw_gesture = "FIST"
                elif up_fingers == 2 and fingers[1] == 1 and fingers[2] == 1:
                    # Index and Middle up only
                    raw_gesture = "REVERSE"
                
                # Correction for "PALM" - if thumb is closed it might be 4 fingers
                if up_fingers >= 3:
                     raw_gesture = "PALM"

                if draw:
                    self.mp_draw.draw_landmarks(
                        image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                    
                    # Draw Gesture Name
                    h, w, c = image.shape
                    cx, cy = int(hand_landmarks.landmark[9].x * w), int(hand_landmarks.landmark[9].y * h)
                    cv2.putText(image, self.stable_gesture, (cx-50, cy-50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # --- STICKY DEBOUNCING LOGIC ---
        # We only switch to a new gesture if it is held for 'stability_threshold' frames.
        
        if raw_gesture == self.stable_gesture:
            # If we see what we already have, reset pending switch
            self.pending_gesture = "NONE"
            self.pending_frames = 0
            
        else:
            # We are seeing something new
            if raw_gesture == self.pending_gesture:
                self.pending_frames += 1
                if self.pending_frames > self.stability_threshold:
                    # Confirmed change!
                    self.stable_gesture = raw_gesture
                    self.pending_frames = 0
            else:
                # New candidate
                self.pending_gesture = raw_gesture
                self.pending_frames = 1
        
        return image, self.stable_gesture

