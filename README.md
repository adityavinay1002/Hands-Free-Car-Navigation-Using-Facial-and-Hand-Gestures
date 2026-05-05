# 🚗 Real-Time Hybrid Car Control System

A cutting-edge real-time gesture recognition system for car control that combines **face-based steering** and **one-hand gesture-based movement**. Built with OpenCV and MediaPipe for efficient, lag-free performance.

---

## 🎯 Features

### 🔄 Control Toggle (NEW)
- **Toggle Control** → Press `T` to turn steering/movement control **ON** or **OFF**.
- Allows you to reposition yourself or adjust settings without sending accidental keyboard inputs.
- Status is clearly displayed in the console and on-screen.

### 📐 Face-Based Steering (Head Tilt)
- **Left Tilt** → Press `A` (Steer Left)
- **Right Tilt** → Press `D` (Steer Right)  
- **Straight Head** → Release `A` and `D` (Drive Straight)
- **Tuned Sensitivity**: Now uses a **10% threshold** (down from 15%) for more responsive and effortless steering.
- Uses MediaPipe FaceMesh for robust, multi-point tracking.

### ✋ One-Hand Gesture Movement Control
- **Open Palm** 🤚 → Press `W` (Accelerate)
- **Closed Fist** ✊ → Press `S` (Brake/Stop)
- **Victory Sign** ✌️ → Press `S` (Reverse)
- Detects a single hand using MediaPipe Hands with high-speed LITE model.
- **Gesture Smoothing**: Advanced debouncing logic for stable, noise-free control.

### 🚀 Performance & Optimization
- **Ultra-Low Latency**: Optimized frame processing for near-instant response.
- **Visual Feedback**: Real-time HUD showing active keys, gestures, and system status.
- **Safe Keys**: Automatically releases all keys on exit or toggle OFF.

---

## 📋 Requirements

- **Python 3.7+**
- **Webcam** (USB or built-in)
- **Windows** (Recommended for PyAutoGUI keyboard simulation)

### Python Dependencies
```bash
pip install opencv-python mediapipe numpy pyautogui
```

---

## 🎮 Usage

### 1. Start the System
```bash
python main.py
```

### 2. Basic Controls
| Action | Gesture/Movement | Key |
| :--- | :--- | :--- |
| **Toggle System** | Press `T` | **ON / OFF** |
| **Accelerate** | Open Palm 🤚 | `W` |
| **Brake/Reverse** | Closed Fist ✊ or Victory Sign ✌️ | `S` |
| **Steer Left** | Tilt Head Left | `A` |
| **Steer Right** | Tilt Head Right | `D` |
| **Exit** | Press `ESC` or `Q` | **Close** |

> [!TIP]
> Use the **'T' key** to pause controls while you are adjusting your seat or camera position to avoid unwanted car movements!

---

## ⚙️ Configuration

The system is pre-tuned for the best balance of speed and stability. You can further customize it in `main.py`:

```python
# Found in CarControlSystem.__init__
self.head_detector = HeadTiltDetector(
    tilt_threshold=0.10,   # Sensitivity: lower = more sensitive
    smoothing=4            # Stability: higher = less jitter
)
```

### Tuning Guide
- **Tilt Threshold (0.10)**: If steering feels too hard, decrease this value (e.g., 0.08). If it's too twitchy, increase it (e.g., 0.12).
- **Smoothing (4-5)**: Increase this if the steering/gestures feel "jittery" due to lighting or camera quality.

---

## 🔍 Troubleshooting

- **Keys Not Registering**: Ensure the game window (GTA V, racing sim, etc.) is the **active window** on your screen.
- **Poor Detection**: Ensure your face and hand are well-lit. Avoid strong backlighting.
- **Camera Lag**: Close other apps using the webcam. Ensure you are using a USB 3.0 port if using an external camera.

---

## 🛠️ Project Structure

- `main.py`: Core logic, UI rendering, and keyboard simulation.
- `face_control.py`: MediaPipe FaceMesh integration for head tracking.
- `hand_control.py`: MediaPipe Hands integration for gesture recognition.

---

## 📄 License
This project is open-source and available for educational and personal use.

**Enjoy the hands-free driving experience! 🚀**
