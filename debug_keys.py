
import pyautogui
import time
import sys

print("Testing PyAutoGUI...")
print("1. Mouse Position:", pyautogui.position())
print("2. Screen Size:", pyautogui.size())

print("3. Testing Key Press (Pressing 'a' 3 times)...")
try:
    # Fail-safe might trigger if mouse is in corner
    pyautogui.FAILSAFE = False
    
    print("   Starting in 3 seconds. Please focus a text field (e.g. Notepad) if you want to see output.")
    for i in range(3, 0, -1):
        print(f"   {i}...")
        time.sleep(1)
        
    pyautogui.press('a')
    time.sleep(0.1)
    pyautogui.press('a')
    time.sleep(0.1)
    pyautogui.press('a')
    print("   ✓ Key press commands sent without error.")
except Exception as e:
    print(f"   ❌ FAILED: {e}")
    sys.exit(1)

print("\nDiagnostics passed.")
