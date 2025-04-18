import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, fleet: "AlienFleet", x: float, y: float):
        super().__init__()

        self.fleet = fleet
        self.settings = fleet.settings
        self.screen = fleet.game.screen
        self.boundaries = self.screen.get_rect()

        # Load and scale the alien image
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_w, self.settings.alien_h)
        )

        # Set the alien's initial position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Use float values for more accurate movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the alien vertically based on the fleet's direction."""
        temp_speed = self.settings.fleet_speed
        self.y += temp_speed * self.fleet.fleet_direction
        self.rect.y = self.y
        self.rect.x = self.x  # Maintain horizontal position during forward shift

    def check_edges(self):
        """Return True if alien has reached top or bottom edge of the screen."""
        return self.rect.top <= 0 or self.rect.bottom >= self.boundaries.bottom

    def draw_alien(self):
        """Draw the alien on the screen at its current position."""
        self.screen.blit(self.image, self.rect)
