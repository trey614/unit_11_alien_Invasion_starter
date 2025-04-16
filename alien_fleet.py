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
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_dropspeed

        self.create_fleet()

    def create_fleet(self):
        alien_h = self.settings.alien_h  # Height of each alien
        alien_w = self.settings.alien_w  # Width of each alien
        screen_h = self.settings.screen_h  # Height of screen
        screen_w = self.settings.screen_w  # Width of screen

        # How many fit vertically (rows) and horizontally (columns)
        fleet_rows = self.calculate_vertical_count(alien_h, screen_h)
        fleet_cols = self.calculate_horizontal_count(alien_w, screen_w)

        # Right-align the fleet by adjusting x_offset to start from the far right
        total_width = fleet_cols * alien_w  # Total width of all columns
        x_offset = screen_w - total_width - 10  # Position fleet to the right with some margin
        y_offset = (screen_h - fleet_rows * alien_h) // 2  # Center fleet vertically

        for col in range(fleet_cols):
            current_x = col * alien_w + x_offset  # Calculate x position for each column
            for row in range(fleet_rows):
                current_y = row * alien_h + y_offset
                current_x = alien_w * col + x_offset
                if row % 2 == 0 or col % 2 == 0:
                    continue  # Calculate y position for each row
                self._create_alien(current_x, current_y)

    def calculate_vertical_count(self, alien_h, screen_h):
        count = screen_h // alien_h  # How many rows fit vertically
        return max(1, count - 2)  # At least 1 row, minus some margin for spacing

    def calculate_horizontal_count(self, alien_w, screen_w):
        count = screen_w // alien_w  # How many columns fit horizontally
        return max(1, count // 4)  # Only use ~1/4 of the screen width for columns

    def _create_alien(self, current_x: int, current_y: int):
        new_alien = Alien(self.game, current_x, current_y)
        self.fleet.add(new_alien)

    def draw(self):
        for alien in self.fleet:
            alien.draw_alien()
