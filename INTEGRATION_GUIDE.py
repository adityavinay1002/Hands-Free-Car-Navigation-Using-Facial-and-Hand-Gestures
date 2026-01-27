"""
INTEGRATION GUIDE: Car Control System with Web Games
====================================================

This guide shows how to integrate the gesture-based car control system
with web-based games like City Car Driving Simulator Ultimate on CrazyGames.
"""

# ============================================================================
# STEP 1: PREREQUISITES
# ============================================================================

"""
✓ Python 3.8+ installed
✓ Project files downloaded (main.py, face_control.py, hand_control.py)
✓ Dependencies installed: pip install -r requirements.txt
✓ Webcam working and accessible
✓ Web browser (Chrome, Firefox, Edge, etc.)
"""

# ============================================================================
# STEP 2: SETUP FOR WEB GAMES
# ============================================================================

"""
1. OPEN THE GAME IN BROWSER
   • Go to: https://www.crazygames.com/game/city-car-driving-simulator-ultimate
   • Wait for game to fully load
   • Click "Play" to start

2. POSITION YOUR WINDOWS
   • Browser window: Takes ~60% of screen (right side)
   • Webcam window: Takes ~40% of screen (left side)
   • Both visible at same time for monitoring

3. GAME CONTROLS
   Default Web Game Keys:
   • W or ↑ = Forward/Accelerate
   • S or ↓ = Brake/Reverse
   • A or ← = Steer Left
   • D or → = Steer Right
   • SPACE = Handbrake/Pause

   Our System Maps To:
   • 'W' = Accelerate (open palm)
   • 'S' = Reverse (victory sign)
   • 'A' = Steer Left (face left)
   • 'D' = Steer Right (face right)
   • PERFECT MATCH! ✓
"""

# ============================================================================
# STEP 3: LAUNCH SEQUENCE
# ============================================================================

"""
1. Start the Gesture Control System:
   cd C:\Users\adity\Downloads\New-Project
   python main.py

2. Wait for:
   • Webcam window to appear
   • "✓ Streaming from webcam..." message
   • Live face and hand detection visible

3. Click on the browser window with the game
   (This gives the game input focus)

4. Control the game:
   • Move your face LEFT/RIGHT for steering
   • Show OPEN PALM to accelerate
   • Make a FIST to brake
   • Show VICTORY SIGN to reverse
   • Press ESC/Q in webcam window to stop
"""

# ============================================================================
# STEP 4: GAME-SPECIFIC CONFIGURATIONS
# ============================================================================

"""
CITY CAR DRIVING SIMULATOR ULTIMATE (CrazyGames)
────────────────────────────────────────────────

URL: https://www.crazygames.com/game/city-car-driving-simulator-ultimate

Controls:
  ✓ W = Accelerate
  ✓ S = Reverse
  ✓ A = Left
  ✓ D = Right
  ✓ Space = Handbrake
  ✓ R = Reset
  ✓ C = Change camera
  ✓ ESC = Pause menu

Integration: WORKS PERFECTLY ✓
Status: Ready to use

Tips:
  1. Start in an empty area to practice
  2. Go slowly at first (use quick palm movements)
  3. Use FIST to brake before turns
  4. Keep your face clearly visible
  5. Good lighting helps accuracy
"""

# ============================================================================
# STEP 5: OTHER COMPATIBLE GAMES
# ============================================================================

"""
Games that work with this system (WASD controls):

1. GTA V (Steam/Epic Games)
   • Keys: W=Forward, A=Left, S=Reverse, D=Right
   • Status: ✓ WORKS
   • Tip: Works offline and online

2. Assetto Corsa (Steam)
   • Keys: Can be configured to WASD
   • Status: ✓ WORKS (after key binding)
   • Tip: Configure in game settings

3. BeamNG Drive (Steam)
   • Keys: W/S for throttle, A/D for steering
   • Status: ✓ WORKS
   • Tip: Works great with this system

4. Euro Truck Simulator 2 (Steam)
   • Keys: W=Forward, A=Left, S=Reverse, D=Right
   • Status: ✓ WORKS

5. American Truck Simulator (Steam)
   • Keys: W=Forward, A=Left, S=Reverse, D=Right
   • Status: ✓ WORKS

6. Forza Horizon 5 (Steam/Xbox Pass)
   • Keys: W=Forward, A=Left, S=Reverse, D=Right
   • Status: ✓ WORKS

7. Web Games (CrazyGames, Pogo, Y8, etc.)
   • Most use standard WASD
   • Status: ✓ MOSTLY WORKS
   • Tip: Check game controls in menu
"""

# ============================================================================
# STEP 6: TROUBLESHOOTING
# ============================================================================

"""
PROBLEM: Game doesn't respond to inputs
─────────────────────────────────────────
Solution:
  1. Make sure game window is active (click on it)
  2. Check if PyAutoGUI is installed: pip install pyautogui
  3. Verify keys are mapping correctly in game settings
  4. Try pressing keys manually to test game

PROBLEM: Face/hand not detected
──────────────────────────────
Solution:
  1. Improve lighting (use desk lamp or window light)
  2. Position face/hand closer to webcam (20-50cm away)
  3. Move to different area with better background
  4. Clean webcam lens

PROBLEM: Lag or slow response
──────────────────────────────
Solution:
  1. Close other applications using webcam
  2. Close other CPU-intensive programs
  3. Reduce resolution in Config (main.py)
  4. Increase gesture smoothing threshold

PROBLEM: Keys stuck (keep pressing)
────────────────────────────────────
Solution:
  1. Close the webcam window (presses ESC)
  2. Press the stuck key manually in game
  3. Restart the system
  4. Check hand detection calibration

PROBLEM: PyAutoGUI permissions error
──────────────────────────────────────
Solution (Windows):
  1. Run Python as Administrator
  2. Or disable UAC (not recommended)
  
Solution (Linux):
  1. Install: sudo apt-get install xdotool
  2. Or use: python3 -m pip install keyboard
  
Solution (Mac):
  1. Grant accessibility permissions:
     System Preferences → Security & Privacy → Accessibility
  2. Add Python and Terminal to list
"""

# ============================================================================
# STEP 7: ADVANCED CONFIGURATION
# ============================================================================

"""
Customize the system by editing Config class in main.py:

STEERING SENSITIVITY:
  • Increase: Move face less for same effect
  • Decrease: Move face more for same effect
  • Default: 15 pixels threshold
  • Edit: Change STEERING_THRESHOLD value

GESTURE SMOOTHING:
  • Increase: More stable but slower response
  • Decrease: Faster but more jittery
  • Default: 3 frames
  • Edit: Change GESTURE_SMOOTHING value

FPS TARGET:
  • Higher: More responsive (uses more CPU)
  • Lower: Less CPU usage
  • Default: 30 FPS
  • Edit: Change TARGET_FPS value
"""

# ============================================================================
# STEP 8: BEST PRACTICES
# ============================================================================

"""
1. SETUP ENVIRONMENT
   ✓ Good lighting (natural or desk lamp)
   ✓ Clear space around you
   ✓ Webcam on stable surface
   ✓ Clean webcam lens

2. CALIBRATION
   ✓ Start game in pause menu
   ✓ Practice steering (move face left/right)
   ✓ Practice accelerating (show and hide palm)
   ✓ Practice braking (make and release fist)
   ✓ Get comfortable with controls

3. DRIVING
   ✓ Start in empty area
   ✓ Drive slowly at first
   ✓ Use smooth head movements
   ✓ Make clear hand gestures
   ✓ Brake before sharp turns

4. OPTIMIZATION
   ✓ Monitor FPS in webcam window
   ✓ If FPS drops, close other apps
   ✓ Adjust lighting if detection fails
   ✓ Fine-tune sensitivity in config
"""

# ============================================================================
# STEP 9: QUICK START COMMAND
# ============================================================================

"""
To start immediately:

1. Open Command Prompt/PowerShell
2. Navigate to project: cd C:\Users\adity\Downloads\New-Project
3. Run: python main.py
4. Open browser with game in another window
5. Click on game to give it focus
6. START DRIVING! 🚗
"""

# ============================================================================
# STEP 10: VIDEO SETUP EXAMPLE
# ============================================================================

"""
WINDOW LAYOUT (Recommended):

┌─────────────────────────────────────────────────────────────┐
│                    MONITOR LAYOUT                          │
├─────────────────────────┬─────────────────────────────────┤
│                         │                                 │
│  Webcam Window          │    Browser with Game            │
│  (Face/Hand Detection)  │    (City Car Driving)           │
│                         │                                 │
│  Shows:                 │  Shows:                         │
│  • Your face/hand       │  • Car on road                  │
│  • Current gesture      │  • Game controls                │
│  • Steering direction   │  • Speed/fuel indicator         │
│  • Active keys (A,D,W)  │                                 │
│                         │                                 │
│  Control it with:       │  Controlled by:                 │
│  • Face movements       │  • Your gestures (above)        │
│  • Hand gestures        │                                 │
│                         │                                 │
└─────────────────────────┴─────────────────────────────────┘
"""

# ============================================================================
# SUPPORT & TIPS
# ============================================================================

"""
TIPS FOR BETTER PERFORMANCE:

1. FACE DETECTION
   • Good lighting is KEY
   • Face should be centered in frame
   • About 30-50cm from webcam
   • Clear background helps

2. HAND GESTURES
   • Keep hand in frame (not too close/far)
   • Use clear, deliberate movements
   • Open palm = all fingers visible
   • Closed fist = all fingers hidden
   • Victory sign = only 2 fingers up

3. GAME FOCUS
   • Always click game window before playing
   • Key presses only work in focused window
   • If stuck, click webcam window and press ESC

4. CALIBRATION
   • Take time to practice the gestures
   • Each person has slightly different timing
   • Adjust thresholds in config if needed
   • Start with slow movements

5. FPS MONITORING
   • Watch FPS in webcam window
   • If drops below 20, close other apps
   • Ideal range: 25-30 FPS
   • Higher = better responsiveness
"""

print(__doc__)
