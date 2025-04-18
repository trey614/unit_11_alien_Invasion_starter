import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """A class to manage bullets fired by the player's ship."""

    def __init__(self, game: 'AlienInvasion'):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load and scale the bullet image
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image, 
            (self.settings.bullet_w, self.settings.bullet_h)
        )

        # Rotate bullet to face rightward (horizontal firing)
        self.image = pygame.transform.rotate(self.image, -90)

        # Set the bullet's initial position at the front of the ship
        self.rect = self.image.get_rect()
        self.rect.midright = game.ship.rect.midright

        # Use a float for more accurate horizontal movement
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet to the right across the screen."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x  # Update the rect position

    def draw_bullet(self):
        """Draw the bullet at its current location on the screen."""
        self.screen.blit(self.image, self.rect)
