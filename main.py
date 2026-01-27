"""
Real-Time Hybrid Car Control System
Face-based steering + Hand gesture-based movement
Pure OpenCV implementation (NO MediaPipe required)
"""

import cv2
import time
import sys

try:
    import pyautogui
    HAS_PYAUTOGUI = True
except ImportError:
    HAS_PYAUTOGUI = False
    print("⚠️  PyAutoGUI not installed. Install with: pip install pyautogui")

from face_control import HeadTiltDetector
from hand_control import HandGestureDetector


class Config:
    """System configuration."""
    TARGET_FPS = 30
    WINDOW_NAME = "Real-Time Hybrid Car Control (OpenCV)"
    DISPLAY_FPS = True


class KeyboardController:
    """Handle keyboard control with PyAutoGUI."""
    
    pressed_keys = set()
    
    @staticmethod
    def configure():
        """Configure PyAutoGUI."""
        if HAS_PYAUTOGUI:
            pyautogui.FAILSAFE = False
    
    @staticmethod
    def press_key(key):
        """Press a key."""
        # Only press if not already pressed, OR if we want to re-assert (but avoid spamming log)
        if HAS_PYAUTOGUI:
            try:
                # If key already pressed, just keep it down, don't spam log
                if key not in KeyboardController.pressed_keys:
                    print(f"[DEBUG] Pressing key: {key}")
                
                pyautogui.keyDown(key)
                KeyboardController.pressed_keys.add(key)
            except Exception as e:
                print(f"[ERROR] Failed to press {key}: {e}")
    
    @staticmethod
    def release_key(key):
        """Release a key."""
        if HAS_PYAUTOGUI and key in KeyboardController.pressed_keys:
            try:
                print(f"[DEBUG] Releasing key: {key}")
                pyautogui.keyUp(key)
                KeyboardController.pressed_keys.discard(key)
            except Exception:
                pass
    
    @staticmethod
    def release_all():
        """Release all keys."""
        for key in list(KeyboardController.pressed_keys):
            if HAS_PYAUTOGUI:
                try:
                    pyautogui.keyUp(key)
                except:
                    pass
        KeyboardController.pressed_keys.clear()


class CarControlSystem:
    """Main car control system."""
    
    def __init__(self):
        """Initialize the system."""
        # Initialize webcam
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise RuntimeError("❌ Error: Could not open webcam.")
        
        # Set camera properties
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        
        # Initialize detectors
        self.head_detector = HeadTiltDetector()
        self.hand_detector = HandGestureDetector()
        
        # Performance tracking
        self.frame_count = 0
        self.fps = 0
        self.start_time = time.time()
        self.prev_frame_time = 0
        
        # State tracking
        self.last_steering_direction = "CENTER"
        self.last_movement_gesture = "NONE"
        
        # Configure keyboard
        KeyboardController.configure()
        
        self._print_instructions()
    
    def _print_instructions(self):
        """Print control instructions."""
        print("\n" + "="*70)
        print("🚗 REAL-TIME HYBRID CAR CONTROL SYSTEM (OpenCV Only)")
        print("="*70)
        print("\n📐 STEERING (Face Position):")
        print("  Face LEFT  → Press 'A'")
        print("  Face RIGHT → Press 'D'")
        print("  Face CENTER → Release A/D")
        print("\n✋ MOVEMENT (Hand Gesture):")
        print("  Open Hand   → Press 'W' (Accelerate)")
        print("  Closed Fist → Brake")
        print("  Victory Sign → Press 'S' (Reverse)")
        print("\n⌨️  Controls:")
        print("  ESC or Q → Exit")
        print("="*70)
        print("✓ Starting camera feed...\n")
    
    def _update_fps(self):
        """Update FPS counter."""
        current_time = time.time()
        if current_time - self.prev_frame_time > 0:
            self.fps = 1 / (current_time - self.prev_frame_time)
        self.prev_frame_time = current_time
        self.frame_count += 1
    
    def _handle_steering(self, direction):
        """
        Handle steering control.
        CONTINUOUS HOLDING: Re-assert key down every frame.
        """
        # Always release conflicting key FIRST
        if direction == "LEFT":
            KeyboardController.release_key('d')
            KeyboardController.press_key('a')
        elif direction == "RIGHT":
            KeyboardController.release_key('a')
            KeyboardController.press_key('d')
        else:  # CENTER
            KeyboardController.release_key('a')
            KeyboardController.release_key('d')
            
        self.last_steering_direction = direction
    
    def _handle_movement(self, gesture):
        """
        Handle movement control.
        CONTINUOUS HOLDING: Re-assert key down every frame.
        """
        # Always release conflicting keys FIRST
        if gesture == "PALM":
             # Accelerate (W)
             KeyboardController.release_key('s')
             KeyboardController.release_key('space')
             KeyboardController.press_key('w')
             
        elif gesture == "FIST":
             # Brake (SPACE)
             KeyboardController.release_key('w')
             KeyboardController.release_key('s')
             KeyboardController.press_key('space')
             
        elif gesture == "REVERSE":
             # Reverse (S)
             KeyboardController.release_key('w')
             KeyboardController.release_key('space')
             KeyboardController.press_key('s')
             
        elif gesture == "NONE":
             # Stop all movement
             KeyboardController.release_key('w')
             KeyboardController.release_key('s')
             KeyboardController.release_key('space')
             
        self.last_movement_gesture = gesture
    
    def _draw_ui(self, frame, direction, gesture):
        """Draw UI on frame."""
        h, w, _ = frame.shape
        
        # Background overlay
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (w, 150), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.4, frame, 0.6, 0, frame)
        
        # FPS
        if Config.DISPLAY_FPS:
            cv2.putText(
                frame,
                f"FPS: {self.fps:.1f}",
                (w - 150, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )
        
        # steering info
        steering_color = {
            "LEFT": (0, 255, 255),
            "RIGHT": (0, 165, 255),
            "CENTER": (0, 255, 0)
        }.get(direction, (255, 255, 255))
        
        steering_symbol = {"LEFT": "◄◄", "RIGHT": "►►", "CENTER": "▶"}
        cv2.putText(
            frame,
            f"STEERING: {steering_symbol.get(direction, '?')} {direction}",
            (10, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            steering_color,
            2
        )
        
        # Movement info
        movement_color = {
            "PALM": (0, 255, 0),
            "FIST": (0, 0, 255),
            "REVERSE": (0, 165, 255),
            "NONE": (128, 128, 128)
        }.get(gesture, (255, 255, 255))
        
        movement_symbol = {"PALM": "🤚", "FIST": "✊", "REVERSE": "✌️", "NONE": ""}
        cv2.putText(
            frame,
            f"MOVEMENT: {gesture}",
            (10, 75),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            movement_color,
            2
        )
        
        # Active keys
        active_keys = list(KeyboardController.pressed_keys)
        keys_str = f"Keys: {', '.join(active_keys).upper()}" if active_keys else "Keys: -"
        cv2.putText(
            frame,
            keys_str,
            (10, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2
        )
        
        # --- NEW: ACTIVE STATUS OVERLAY ---
        # Draw a big visible status notification in the center/bottom
        status_text = ""
        status_color = (128, 128, 128)
        
        if "w" in active_keys:
            status_text = "ACCELERATING (W)"
            status_color = (0, 255, 0) # Green
        elif "s" in active_keys:
            status_text = "REVERSING (S)"
            status_color = (0, 165, 255) # Orange
        elif gesture == "FIST":
            status_text = "BRAKING (FIST)"
            status_color = (0, 0, 255) # Red
            
        if status_text:
            # Draw center bottom box
            text_size = cv2.getTextSize(status_text, cv2.FONT_HERSHEY_SIMPLEX, 1.0, 3)[0]
            cx = w // 2 - text_size[0] // 2
            cy = h - 50
            
            # Box background
            cv2.rectangle(frame, (cx - 20, cy - 40), (cx + text_size[0] + 20, cy + 20), (0, 0, 0), -1)
            # Text
            cv2.putText(frame, status_text, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 1.0, status_color, 3)

        # Exit instruction
        cv2.putText(
            frame,
            "Press ESC or Q to exit",
            (w - 300, h - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (100, 100, 100),
            1
        )
        
        return frame
    
    def run(self):
        """Main control loop."""
        try:
            print("✓ Detectors initialized")
            print("✓ Keyboard controller ready")
            print("✓ Streaming from webcam...\n")
            
            while True:
                success, frame = self.cap.read()
                if not success:
                    continue
                
                # Flip for selfie view
                frame = cv2.flip(frame, 1)
                
                # Detect head position for steering
                frame, steering_direction = self.head_detector.detect_tilt(frame, draw=True)
                
                # Detect hand gesture for movement
                frame, movement_gesture = self.hand_detector.detect_gesture(frame, draw=True)
                
                # Apply control
                self._handle_steering(steering_direction)
                self._handle_movement(movement_gesture)
                
                # Draw UI
                frame = self._draw_ui(frame, steering_direction, movement_gesture)
                
                # Update FPS
                self._update_fps()
                
                # Show frame
                cv2.imshow(Config.WINDOW_NAME, frame)
                
                # Handle input
                key = cv2.waitKey(1) & 0xFF
                if key == 27 or key == ord('q'):  # ESC or Q
                    print("\n⏹️  Closing application...")
                    break
                
        except KeyboardInterrupt:
            print("\n⏹️  Interrupted by user")
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
        finally:
            self._cleanup()
    
    def _cleanup(self):
        """Clean up resources."""
        print("🔄 Cleaning up...")
        KeyboardController.release_all()
        self.cap.release()
        cv2.destroyAllWindows()
        print("✓ Camera released")
        print("✓ All keys released")
        print(f"✓ Processed {self.frame_count} frames")
        print(f"✓ Average FPS: {self.frame_count / (time.time() - self.start_time):.1f}\n")


def main():
    """Entry point."""
    try:
        system = CarControlSystem()
        system.run()
    except RuntimeError as e:
        print(f"❌ {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
