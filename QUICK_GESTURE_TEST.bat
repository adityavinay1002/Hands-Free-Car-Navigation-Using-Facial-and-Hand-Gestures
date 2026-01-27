@echo off
REM Quick Gesture Test - Run this to immediately see if gestures work

echo.
echo ========================================
echo   GESTURE DETECTION QUICK TEST
echo ========================================
echo.

cd /d "%~dp0"

echo Testing gesture detection...
echo.
echo Instructions:
echo   1. Show your HAND in the camera
echo   2. Watch for GREEN CONTOUR around hand
echo   3. System will show detected gesture
echo.
echo Press 'q' or ESC to exit
echo.
pause

python -u test_gestures.py

if %errorlevel% neq 0 (
    echo.
    echo ERROR running test. Make sure:
    echo   1. Python is installed
    echo   2. opencv-python is installed: pip install opencv-python
    echo   3. Camera is connected and working
    echo.
    pause
)
