
try:
    import mediapipe
    print("✓ MediaPipe is installed")
    from hand_control import HandGestureDetector
    print("✓ HandGestureDetector imported successfully")
except ImportError as e:
    print(f"❌ Error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
