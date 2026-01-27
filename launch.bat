@echo off
REM ============================================================================
REM QUICK LAUNCHER FOR CAR CONTROL SYSTEM
REM ============================================================================

title Gesture-Based Car Control System
color 0A

cls
echo.
echo ======================================================================
echo        GESTURE-BASED CAR CONTROL SYSTEM - LAUNCHER
echo ======================================================================
echo.
echo Project Location: C:\Users\adity\Downloads\New-Project
echo.
echo What would you like to do?
echo.
echo 1) Run Car Control System (play games now!)
echo 2) Open City Car Driving Game in Browser
echo 3) View Quick Start Guide
echo 4) Install Dependencies
echo 5) Run Setup Wizard
echo 6) Exit
echo.
echo ======================================================================
echo.

setlocal enabledelayedexpansion

set /p choice="Enter your choice (1-6): "

if "%choice%"=="1" (
    echo.
    echo Launching Car Control System...
    echo.
    python main.py
    pause
    goto menu
)

if "%choice%"=="2" (
    echo.
    echo Opening City Car Driving Simulator in browser...
    echo.
    start https://www.crazygames.com/game/city-car-driving-simulator-ultimate
    echo.
    echo Browser opened! Now run Car Control System in another window.
    echo Command: python main.py
    echo.
    pause
    goto menu
)

if "%choice%"=="3" (
    echo.
    more QUICK_START.md
    goto menu
)

if "%choice%"=="4" (
    echo.
    echo Installing dependencies...
    echo.
    pip install -r requirements.txt
    echo.
    pause
    goto menu
)

if "%choice%"=="5" (
    echo.
    echo Running Setup Wizard...
    echo.
    python setup.py
    pause
    goto menu
)

if "%choice%"=="6" (
    echo.
    echo Goodbye!
    echo.
    exit /b 0
)

echo Invalid choice. Please try again.
pause
goto menu

:menu
cls
goto start
