import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    """Manages the group of alien enemies in the game."""

    def __init__(self, game: "AlienInvasion"):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction  # 1 for down, -1 for up
        self.fleet_drop_speed = self.settings.fleet_dropspeed  # How far to move left each bounce

        self.create_fleet()

    def create_fleet(self):
        """Create a fleet of aliens aligned in vertical columns on the right side."""
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_cols = 3  # Number of vertical alien lines
        fleet_rows = (screen_h - 2 * alien_h) // alien_h  # Max number of rows to fit on screen

        # Start positions to align fleet to the far right of the screen
        x_start = screen_w - (fleet_cols * alien_w) - 10
        y_start = (screen_h - (fleet_rows * alien_h)) // 2

        # Create aliens in a grid of columns and rows
        for col in range(fleet_cols):
            for row in range(fleet_rows):
                x = x_start + col * alien_w
                y = y_start + row * alien_h
                self._create_alien(x, y)

    def _create_alien(self, x: int, y: int):
        """Helper method to create and add a single alien to the fleet."""
        alien = Alien(self, x, y)
        self.fleet.add(alien)

    def _check_fleet_edges(self):
        """Reverse direction and move left when any alien reaches top or bottom edge."""
        for alien in self.fleet:
            if alien.check_edges():
                self.fleet_direction *= -1  # Change vertical movement direction
                self._advance_fleet()
                break

    def _advance_fleet(self):
        """Move the entire fleet left by a fixed distance."""
        for alien in self.fleet:
            alien.x -= self.fleet_drop_speed
            alien.rect.x = alien.x

    def update_fleet(self):
        """Update the position of all aliens in the fleet."""
        self._check_fleet_edges()
        self.fleet.update()
      
    def draw(self):
        """Draw all aliens in the fleet to the screen."""
        for alien in self.fleet:
            alien.draw_alien()
    
    def check_fleet_left(self):
        """Check if any alien has moved past the left edge of the screen."""
        for alien in self.fleet:
            if alien.rect.left >= self.settings.screen_w:
                return True
        return False

    def check_destroyed_status(self):
        """Return True if all aliens have been destroyed."""
        return not self.fleet
