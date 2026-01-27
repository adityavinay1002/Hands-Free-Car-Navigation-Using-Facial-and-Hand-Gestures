#!/usr/bin/env python3
"""
Quick Setup Script - Set up and launch the car control system
"""

import os
import sys
import webbrowser
import time
import subprocess


def print_header():
    """Print welcome header."""
    print("\n" + "="*70)
    print("🚗 GESTURE-BASED CAR CONTROL SYSTEM - SETUP WIZARD 🚗")
    print("="*70 + "\n")


def print_menu():
    """Print main menu."""
    print("SELECT OPTION:")
    print("-" * 70)
    print("1. Run Car Control System (main.py)")
    print("2. View Game Integration Guide")
    print("3. List Compatible Games & Configurations")
    print("4. Open City Car Driving Game in Browser")
    print("5. Install Dependencies")
    print("6. Exit")
    print("-" * 70)


def run_main():
    """Run the main car control system."""
    print("\n🎬 Launching Car Control System...\n")
    time.sleep(1)
    
    try:
        subprocess.run([sys.executable, "main.py"])
    except KeyboardInterrupt:
        print("\n✓ Car control system stopped")


def show_guide():
    """Show integration guide."""
    print("\n📖 INTEGRATION GUIDE:")
    print("="*70)
    try:
        with open("INTEGRATION_GUIDE.py", "r") as f:
            content = f.read()
            # Extract docstring
            if '"""' in content:
                start = content.find('"""') + 3
                end = content.find('"""', start)
                print(content[start:end])
    except FileNotFoundError:
        print("❌ INTEGRATION_GUIDE.py not found")
    print("="*70)


def show_games():
    """Show compatible games."""
    try:
        from game_config import list_all_games
        list_all_games()
    except ImportError:
        print("❌ game_config.py not found")


def open_game():
    """Open City Car Driving game in browser."""
    print("\n🌐 Opening City Car Driving Simulator Ultimate...")
    print("⏳ Please wait, browser will open...\n")
    
    url = "https://www.crazygames.com/game/city-car-driving-simulator-ultimate"
    
    try:
        webbrowser.open(url)
        print("✓ Browser opened with game")
        print("\nNext steps:")
        print("1. Click 'Play' to start the game")
        print("2. Open another terminal/command prompt")
        print("3. Run: python main.py")
        print("4. Position windows side by side")
        print("5. Click game window to give it focus")
        print("6. Start driving with gestures!")
    except Exception as e:
        print(f"❌ Error opening browser: {e}")
        print(f"\nManually open: {url}")


def install_deps():
    """Install dependencies."""
    print("\n📦 Installing dependencies...\n")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("\n✓ Dependencies installed successfully")
    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")


def main():
    """Main function."""
    while True:
        print_header()
        print_menu()
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            run_main()
        elif choice == "2":
            show_guide()
        elif choice == "3":
            show_games()
        elif choice == "4":
            open_game()
        elif choice == "5":
            install_deps()
        elif choice == "6":
            print("\n👋 Goodbye!\n")
            sys.exit(0)
        else:
            print("❌ Invalid choice. Please try again.")
        
        input("\nPress ENTER to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Exiting...\n")
        sys.exit(0)
