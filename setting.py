from pathlib import Path

class Settings:
    """Stores all configuration settings for the Alien Invasion game."""

    def __init__(self):
        # Game window settings
        self.name: str = "Alien Invasion"         # Window title
        self.screen_w = 1200                      # Width of the game window
        self.screen_h = 800                       # Height of the game window
        self.FPS = 60      
                           # Frames per second

        # Background settings
        self.bg_file = Path.cwd() / "Assets" / "images" / "Starbasesnow.png"  # Background image path
        self.difficulty_scale = 1.1

        # Ship settings
        self.ship_file = Path.cwd() / "Assets" / "images" / 'ship2(no bg).png'  # Ship image path
        self.ship_w = 40                            # Ship width
        self.ship_h = 60                            # Ship height
        self.ship_speed = 5                         # Ship movement speed
        self.ship_angle = 90                        # Initial angle (if rotated)
        self.starting_ship_count = 3                # Number of lives/ships

        # Bullet (laser) settings
        self.bullet_file = Path.cwd() / "Assets" / "images" / "laserBlast.png"  # Bullet image path
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "laser.mp3"        # Sound for firing
        self.impact_sound = Path.cwd() / "Assets"/ "sound" / "impactSound.mp3"  # Sound for impacts

        self.bullet_speed = 7                       # Speed of bullets
        self.bullet_w = 25                          # Bullet width
        self.bullet_h = 80                          # Bullet height
        self.bullet_amount = 5                      # Max number of bullets allowed on screen

        # Alien fleet settings
        self.alien_file = Path.cwd() / "Assets" / "images" / "enemy_4.png"  # Alien image path
        self.fleet_speed = 5                     # Speed of the alien fleet's vertical movement
        self.alien_w = 30                            # Alien width
        self.alien_h = 20                            # Alien height
        self.fleet_direction = 1                     # Fleet movement direction: 1 = down, -1 = up
        self.fleet_dropspeed = 50                    # Horizontal advancement when reaching top/bottom

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0,135,50)

        self.text_color = (255,255,255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / "Assets" / "Fonts" / "Silkscreen" / "Silkscreen-Bold.ttf"

    def initialize_dynamic_settings(self):
        self.ship_speed = 5
        self.starting_ship_count = 3
        self.bullet_speed = 7
        self.bullet_amount = 5
        self.fleet_speed = 2
        self.fleet_drop_speed = 40
        self.bullet_w = 25
        self.bullet_h = 80

    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bulett_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
