from pathlib import Path

class Settings:

    def __init__(self):
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800  
        self.FPS = 60
        self.bg_file = Path.cwd() / "Assets" / "images" / "Starbasesnow.png"

        self.ship_file = Path.cwd() / "Assets" / "images" / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5
        self.ship_angle = 90


        self.bullet_file = Path.cwd() / "Assets" / "images" / "laserBlast.png"
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "laser.mp3"
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        self.alien_file = Path.cwd() / "Assets" / "images" / "enemy_4.png"
        self.fleet_speed = 5
        self.alien_w= 40
        self.alien_h=40
        self.fleet_direction = 1
        self.fleet_dropspeed = 50
