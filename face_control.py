"""
Face-Based Steering Control - MEDIAPIPE VERSION
Uses MediaPipe Face Mesh for robust head tracking.
"""

import cv2
import mediapipe as mp
import numpy as np

class HeadTiltDetector:
    """Detects head position using MediaPipe Face Mesh."""
    
    def __init__(self, tilt_threshold=0.15, smoothing=5):
        """
        Initialize MediaPipe Face Mesh.
        tilt_threshold: Percentage of screen width to trigger turn (0.15 = 15%)
        """
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
        self.drawing_spec = self.mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
        
        self.tilt_threshold = tilt_threshold # 15% from center
        self.current_direction = "CENTER"
        
        # Smoothing
        self.stability_threshold = smoothing
        self.stable_direction = "CENTER"
        self.pending_direction = "CENTER"
        self.pending_frames = 0
        
    def detect_tilt(self, image, draw=True):
        """
        Detect head position based on NOSE landmark x-coordinate.
        """
        h, w, _ = image.shape
        
        # Convert to RGB
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(img_rgb)
        
        raw_direction = "CENTER"
        
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Get Nose Tip (Landmark 1)
                nose = face_landmarks.landmark[1]
                nose_x = int(nose.x * w)
                nose_y = int(nose.y * h)
                
                # Center X
                center_x = w // 2
                
                # Calculate displacement
                displacement = nose_x - center_x
                
                # Threshold logic (Movement to LEFT or RIGHT)
                limit = int(w * self.tilt_threshold)
                
                if displacement < -limit:
                    raw_direction = "LEFT"
                elif displacement > limit:
                    raw_direction = "RIGHT"
                else:
                    raw_direction = "CENTER"
                
                if draw:
                    # Draw mesh (lightweight)
                    self.mp_drawing.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=self.mp_face_mesh.FACEMESH_TESSELATION,
                        landmark_drawing_spec=self.drawing_spec,
                        connection_drawing_spec=self.drawing_spec)
                    
                    # Draw Nose & Center Line
                    cv2.line(image, (center_x, 0), (center_x, h), (100, 100, 100), 1)
                    cv2.line(image, (center_x - limit, 0), (center_x - limit, h), (0, 255, 255), 1) # Left Threshold
                    cv2.line(image, (center_x + limit, 0), (center_x + limit, h), (0, 255, 255), 1) # Right Threshold
                    
                    cv2.circle(image, (nose_x, nose_y), 8, (0, 0, 255), -1)
                    
                    # Draw Direction Arrow
                    if raw_direction == "LEFT":
                        cv2.arrowedLine(image, (center_x, nose_y), (nose_x, nose_y), (0, 255, 0), 4)
                    elif raw_direction == "RIGHT":
                        cv2.arrowedLine(image, (center_x, nose_y), (nose_x, nose_y), (0, 255, 0), 4)

                    cv2.putText(image, f"Nose X: {nose_x}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
                
                # Only use first face
                break
        
        # --- STICKY DEBOUNCING LOGIC ---
        
        if raw_direction == self.stable_direction:
            # If we see what we already have, reset pending switch
            self.pending_direction = "CENTER" # Arbitrary reset
            self.pending_frames = 0
            
        else:
            # We are seeing something new
            if raw_direction == self.pending_direction:
                self.pending_frames += 1
                if self.pending_frames > self.stability_threshold:
                    # Confirmed change!
                    self.stable_direction = raw_direction
                    self.pending_frames = 0
            else:
                # New candidate
                self.pending_direction = raw_direction
                self.pending_frames = 1
        
        return image, self.stable_direction
