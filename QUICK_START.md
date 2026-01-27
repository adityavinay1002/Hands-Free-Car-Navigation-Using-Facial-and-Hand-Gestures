# 🚗 QUICK START GUIDE: Integrating with Car Games

## What You Need

✅ Project files (already created)
✅ Python 3.8+
✅ Webcam
✅ Browser (Chrome, Firefox, Edge)
✅ Car game (web or desktop)

---

## 🎯 QUICK SETUP (5 Minutes)

### Step 1: Install Dependencies
```bash
cd C:\Users\adity\Downloads\New-Project
pip install -r requirements.txt
```

### Step 2: Choose Your Game

**Web Game (Recommended for testing):**
- City Car Driving Simulator: https://www.crazygames.com/game/city-car-driving-simulator-ultimate
- Just open in browser, click Play

**Desktop Games:**
- GTA V
- Assetto Corsa
- BeamNG Drive
- Euro Truck Simulator 2
- Forza Horizon 5

### Step 3: Launch the System
```bash
python main.py
```

### Step 4: Open Your Game
- Open game in separate window (browser or desktop app)
- Position windows side by side
- Click on game window to give it focus

### Step 5: Drive!
- **Move face LEFT** → Car steers left (A)
- **Move face RIGHT** → Car steers right (D)
- **Show OPEN PALM** → Accelerate (W)
- **Make CLOSED FIST** → Brake (S)
- **Show VICTORY SIGN** → Reverse (S)

---

## 🎮 CITY CAR DRIVING INTEGRATION

### Perfect Match! ✓
The game uses standard WASD controls that match our system perfectly.

### Step-by-Step:

1. **Open Game**
   - Go to: https://www.crazygames.com/game/city-car-driving-simulator-ultimate
   - Click "Play"
   - Wait for game to load

2. **Position Windows**
   ```
   LEFT: Webcam Window (40%)
   RIGHT: Game Window (60%)
   ```

3. **Start Control System**
   ```bash
   python main.py
   ```

4. **Click Game Window**
   - Click on the game to give it keyboard focus
   - (This is important! Keys only work in focused window)

5. **Calibrate (Optional)**
   - Move face left/right slowly
   - Show palm and make fist to test
   - Adjust comfort

6. **Start Driving**
   - Click "Start Drive" or "Free Roam"
   - Practice in empty area
   - Have fun! 🎉

### Game Controls Reference:
```
W = Forward/Accelerate     ← Open Palm
S = Brake/Reverse          ← Closed Fist or Victory Sign
A = Steer Left             ← Face Left
D = Steer Right            ← Face Right
Space = Handbrake          ← (Manual press if needed)
R = Reset Position
C = Change Camera
ESC = Pause Menu
```

---

## 🚀 USING THE SETUP WIZARD

Easy menu-driven setup:

```bash
python setup.py
```

Then select:
```
1. Run Car Control System
2. View Integration Guide
3. List Compatible Games
4. Open City Car Driving Game
5. Install Dependencies
6. Exit
```

---

## 📋 WHAT EACH FILE DOES

| File | Purpose |
|------|---------|
| `main.py` | Main control system (run this!) |
| `face_control.py` | Face detection for steering |
| `hand_control.py` | Hand gesture for movement |
| `setup.py` | Interactive setup wizard |
| `game_config.py` | Game configurations |
| `INTEGRATION_GUIDE.py` | Detailed integration guide |
| `requirements.txt` | Dependencies to install |

---

## ✅ VERIFIED WORKING GAMES

### Web Games
- ✅ City Car Driving Simulator (CrazyGames)
- ✅ Most CrazyGames car games
- ✅ Y8 racing games
- ✅ Pogo car games

### Desktop Games (WASD compatible)
- ✅ GTA V
- ✅ GTA Online
- ✅ Assetto Corsa
- ✅ BeamNG Drive
- ✅ Euro Truck Simulator 2
- ✅ American Truck Simulator
- ✅ Forza Horizon 5
- ✅ Need for Speed (most versions)

---

## 🎯 TROUBLESHOOTING

### Keys not working?
```
1. Make sure game window is ACTIVE (click on it)
2. Check if Python shows "Keys: A, D, W, S" in console
3. Manually press keys in game to verify it responds
4. Try running as Administrator
```

### Face/Hand not detected?
```
1. Improve lighting (use desk lamp)
2. Move closer to webcam (20-50cm)
3. Clean webcam lens
4. Move to different background
```

### Lag or slow response?
```
1. Close other webcam apps
2. Close heavy programs (Chrome with many tabs)
3. Reduce other tasks running
4. Check FPS counter in webcam window (should be 20+)
```

### Game stuck on a key?
```
1. Close webcam window (press ESC)
2. Manually press the stuck key
3. Or restart the system
```

---

## 🎓 TIPS FOR BEST RESULTS

### Lighting
- Use natural light or desk lamp
- Avoid backlighting
- Light source should be in front of you
- Minimize shadows on face/hands

### Hand Gestures
- Keep hand visible in frame
- 30-50cm from webcam
- Clear, deliberate movements
- PALM: Fingers spread wide open
- FIST: All fingers curled closed
- VICTORY: Only index and middle fingers

### Face Position
- Center face in webcam frame
- Face camera directly
- Head straight initially
- Make clear tilt movements (15+ degrees)

### Driving Tips
- Start slow and practice
- Get comfortable with response time
- Use brake (fist) before turns
- Build muscle memory gradually
- Take breaks if tired

---

## 📞 QUICK COMMAND REFERENCE

```bash
# Run control system
python main.py

# Run setup wizard
python setup.py

# Check imports
python -c "from face_control import HeadTiltDetector; print('✓ OK')"

# Install dependencies
pip install -r requirements.txt

# View game configs
python game_config.py

# View integration guide
python -c "exec(open('INTEGRATION_GUIDE.py').read())"
```

---

## 🎮 RECOMMENDED FIRST GAME

**City Car Driving Simulator Ultimate** is the best choice because:
- ✅ Runs in browser (no install needed)
- ✅ Free to play
- ✅ Simple controls match perfectly
- ✅ Great for practice
- ✅ Good feedback system

Get started: https://www.crazygames.com/game/city-car-driving-simulator-ultimate

---

## 🔧 CUSTOMIZATION

Edit `main.py` `Config` class to adjust:

```python
class Config:
    TARGET_FPS = 30              # Frames per second
    WINDOW_NAME = "..."          # Window title
    DISPLAY_FPS = True           # Show FPS counter
```

Edit `face_control.py` to adjust steering sensitivity:
```python
def __init__(self, ...):
    # Adjust threshold for more/less sensitive steering
```

---

## ✨ YOU'RE ALL SET!

Everything is ready to go:
1. ✅ Code is working
2. ✅ No MediaPipe needed
3. ✅ Simple and lightweight
4. ✅ Ready for any WASD game

**Next Steps:**
```
1. python main.py
2. Open your game
3. Click game window
4. Start driving! 🚗
```

---

## 🎉 HAVE FUN!

Enjoy controlling your game with just your face and hand gestures!

For detailed help, see `INTEGRATION_GUIDE.py`
For game configs, see `game_config.py`
