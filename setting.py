from pathlib import Path

class Settings:
    """Stores all configuration settings for the Alien Invasion game."""

    def __init__(self):
        """Initialize static (non-changing) settings for the game."""
        
        # --- Game window settings ---
        self.name: str = "Alien Invasion"             # Title displayed on the game window
        self.screen_w = 1200                          # Width of the game screen in pixels
        self.screen_h = 800                           # Height of the game screen in pixels
        self.FPS = 60                                 # Target frames per second for smooth gameplay

        # --- Background and data file paths ---
        self.bg_file = Path.cwd() / "Assets" / "images" / "Starbasesnow.png"   # Background image path
        self.scores_file = Path.cwd() / "Assets" / "file" / "scores.json"      # High scores file path

        # --- Difficulty settings ---
        self.difficulty_scale = 3.1                   # Multiplier to increase difficulty over time

        # --- Ship settings ---
        self.ship_file = Path.cwd() / "Assets" / "images" / "ship2(no bg).png"  # Ship image path
        self.ship_w = 40                              # Width of the ship sprite
        self.ship_h = 60                              # Height of the ship sprite
        self.ship_speed = 5                           # Movement speed of the ship (can be changed dynamically)
        self.ship_angle = 90                          # Starting angle of the ship (for rotations)
        self.starting_ship_count = 3                  # Initial number of ships/lives

        # --- Bullet (laser) settings ---
        self.bullet_file = Path.cwd() / "Assets" / "images" / "laserBlast.png"  # Bullet image path
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "laser.mp3"        # Sound when firing a bullet
        self.impact_sound = Path.cwd() / "Assets" / "sound" / "impactSound.mp3" # Sound when a bullet hits an alien

        self.bullet_speed = 7                         # Bullet movement speed
        self.bullet_w = 25                            # Bullet width (adjusted dynamically in-game)
        self.bullet_h = 80                            # Bullet height
        self.bullet_amount = 5                        # Max bullets allowed on screen at once

        # --- Alien fleet settings ---
        self.alien_file = Path.cwd() / "Assets" / "images" / "enemy_4.png"      # Alien sprite image path
        self.alien_w = 30                             # Alien width
        self.alien_h = 20                             # Alien height
        self.fleet_speed = 5                          # Initial vertical movement speed of the alien fleet
        self.fleet_direction = 1                      # 1 = down, -1 = up
        self.fleet_dropspeed = 50                     # Distance fleet moves horizontally when bouncing

        # --- Button settings ---
        self.button_w = 200                           # Width of the play button
        self.button_h = 50                            # Height of the play button
        self.button_color = (0, 135, 50)              # Button background color (RGB)

        # --- HUD and font settings ---
        self.text_color = (255, 255, 255)             # Text color (white)
        self.button_font_size = 48                    # Font size for button text
        self.HUD_font_size = 20                       # Font size for HUD elements (score, level, etc.)
        self.font_file = Path.cwd() / "Assets" / "Fonts" / "Silkscreen" / "Silkscreen-Bold.ttf"  # HUD font path

    def initialize_dynamic_settings(self):
        """
        Initialize settings that change throughout the game.
        This is called at the start and when restarting after game over.
        """
        self.ship_speed = 5
        self.starting_ship_count = 3
        self.bullet_speed = 7
        self.bullet_amount = 5
        self.fleet_speed = 2
        self.fleet_drop_speed = 40
        self.alien_points = 50
        self.bullet_w = 250   # Longer laser beam look
        self.bullet_h = 80

    def increase_difficulty(self):
        """
        Increase difficulty by scaling movement speeds.
        Called after completing a level or wave.
        """
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
