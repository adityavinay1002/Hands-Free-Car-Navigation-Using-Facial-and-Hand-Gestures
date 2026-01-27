
try:
    print("Importing mediapipe...")
    import mediapipe
    print("Success")
except Exception as e:
    print(f"FAIL: {e}")
    import traceback
    traceback.print_exc()
