"""
GAME CONFIGURATION FILE
Map different games to their key configurations
"""

# Game profiles with their key mappings
GAME_CONFIGS = {
    "city_car_driving": {
        "name": "City Car Driving Simulator Ultimate",
        "platform": "Web (CrazyGames)",
        "url": "https://www.crazygames.com/game/city-car-driving-simulator-ultimate",
        "keys": {
            "forward": "w",
            "brake": "s",
            "left": "a",
            "right": "d",
            "handbrake": "space",
        },
        "status": "✓ FULLY COMPATIBLE",
        "notes": "Works perfectly, no configuration needed"
    },
    
    "gta_v": {
        "name": "Grand Theft Auto V",
        "platform": "Steam / Epic Games",
        "keys": {
            "forward": "w",
            "brake": "s",
            "left": "a",
            "right": "d",
            "handbrake": "space",
        },
        "status": "✓ FULLY COMPATIBLE",
        "notes": "Works in single-player and online"
    },
    
    "assetto_corsa": {
        "name": "Assetto Corsa",
        "platform": "Steam",
        "keys": {
            "forward": "w",
            "brake": "s",
            "left": "a",
            "right": "d",
            "handbrake": "space",
        },
        "status": "✓ COMPATIBLE (Configure in game)",
        "notes": "Configure controls in game settings first"
    },
    
    "beamng": {
        "name": "BeamNG Drive",
        "platform": "Steam",
        "keys": {
            "forward": "w",
            "brake": "s",
            "left": "a",
            "right": "d",
            "handbrake": "space",
        },
        "status": "✓ FULLY COMPATIBLE",
        "notes": "Excellent for testing, very responsive"
    },
    
    "euro_truck": {
        "name": "Euro Truck Simulator 2",
        "platform": "Steam",
        "keys": {
            "forward": "w",
            "brake": "s",
            "left": "a",
            "right": "d",
            "handbrake": "space",
        },
        "status": "✓ FULLY COMPATIBLE",
        "notes": "Long drives are fun with gestures!"
    },
    
    "american_truck": {
        "name": "American Truck Simulator",
        "platform": "Steam",
        "keys": {
            "forward": "w",
            "brake": "s",
            "left": "a",
            "right": "d",
            "handbrake": "space",
        },
        "status": "✓ FULLY COMPATIBLE",
        "notes": "Similar to Euro Truck"
    },
    
    "forza_horizon_5": {
        "name": "Forza Horizon 5",
        "platform": "Steam / Xbox Pass",
        "keys": {
            "forward": "w",
            "brake": "s",
            "left": "a",
            "right": "d",
            "handbrake": "space",
        },
        "status": "✓ FULLY COMPATIBLE",
        "notes": "High-speed racing, very fun!"
    },
    
    "need_for_speed": {
        "name": "Need for Speed (various)",
        "platform": "EA Origin",
        "keys": {
            "forward": "w",
            "brake": "s",
            "left": "a",
            "right": "d",
            "handbrake": "space",
        },
        "status": "✓ COMPATIBLE (Configure in game)",
        "notes": "Check game control settings"
    },
}


def get_game_config(game_key):
    """Get configuration for a specific game."""
    return GAME_CONFIGS.get(game_key.lower())


def list_all_games():
    """List all supported games."""
    print("\n" + "="*70)
    print("SUPPORTED GAMES & CONFIGURATIONS")
    print("="*70 + "\n")
    
    for key, config in GAME_CONFIGS.items():
        print(f"Game: {config['name']}")
        print(f"Platform: {config['platform']}")
        print(f"Status: {config['status']}")
        print(f"Keys: W={config['keys']['forward']}, A={config['keys']['left']}, "
              f"S={config['keys']['brake']}, D={config['keys']['right']}")
        print(f"Notes: {config['notes']}")
        print("-" * 70)
    
    print("\nAll games use standard WASD controls:")
    print("  • W = Forward/Accelerate")
    print("  • A = Steer Left")
    print("  • S = Brake/Reverse")
    print("  • D = Steer Right")
    print("="*70 + "\n")


# Show list when imported
if __name__ == "__main__":
    list_all_games()
