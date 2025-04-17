import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    def __init__(self, game: "AlienInvasion"):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction  # 1 for down, -1 for up
        self.fleet_drop_speed = self.settings.fleet_dropspeed  # amount to move left each bounce

        self.create_fleet()

    def create_fleet(self):
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_cols = 3  # Number of vertical alien lines
        fleet_rows = (screen_h - 2 * alien_h) // alien_h  # Fit as many vertically as possible

        # Align to far right
        x_start = screen_w - (fleet_cols * alien_w) - 10
        y_start = (screen_h - (fleet_rows * alien_h)) // 2

        for col in range(fleet_cols):
            for row in range(fleet_rows):
                x = x_start + col * alien_w
                y = y_start + row * alien_h
                self._create_alien(x, y)

    def _create_alien(self, x: int, y: int):
        alien = Alien(self, x, y)
        self.fleet.add(alien)

    def _check_fleet_edges(self):
        """Reverse direction and shift left when any alien hits top or bottom."""
        for alien in self.fleet:
            if alien.check_edges():
                self.fleet_direction *= -1  # Reverse vertical direction
                self._advance_fleet()
                break

    def _advance_fleet(self):
        """Shift entire fleet left by drop speed."""
        for alien in self.fleet:
            alien.x -= self.fleet_drop_speed
            alien.rect.x = alien.x

    def update_fleet(self):
        self._check_fleet_edges()
        self.fleet.update()
      
    def draw(self):
        for alien in self.fleet:
            alien.draw_alien()
    
    def check_fleet_left(self):
        alien: Alien
        for alien in self.fleet:
            if alien.rect.left >= self.settings.screen_w:
                return True
        return False