import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion'):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load the bullet image and scale it based on settings
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image, 
            (self.settings.bullet_w, self.settings.bullet_h)
        )
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.rotate(self.image, -90)
        # Get the rectangle of the image and set its starting position
        self.rect = self.image.get_rect()
        self.rect.midright = game.ship.rect.midright

        # Use a floating point for precise movement
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""
        self.x += self.settings.bullet_speed  # Move the bullet upwards
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)



