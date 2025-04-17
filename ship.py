import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import ShipArsenal

class Ship:
    """A class to manage the player's ship."""

    def __init__(self, game: "AlienInvasion", arsenal: "ShipArsenal"):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        # Load and rotate ship image
        self.original_image = pygame.image.load(self.settings.ship_file)
        self.original_image = pygame.transform.scale(
            self.original_image, 
            (self.settings.ship_w, self.settings.ship_h)
        )
        self.image = pygame.transform.rotate(self.original_image, -90)

        # Get the image rectangle and center it
        self.rect = self.image.get_rect()
        self.rect.midleft = self.boundaries.midleft

        # Set float position for smooth movement
        self._center_ship()
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Link to arsenal
        self.arsenal = arsenal

    def _center_ship(self):
        self.rect.midleft = self.boundaries.midleft
        self.x = float(self.rect.x)

    def update(self):
        temp_speed = self.settings.ship_speed

        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed

        self.rect.x = self.x
        self.rect.y = self.y

        self.arsenal.update_arsenal()

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def fire(self):
        return self.arsenal.fire_bullet()

    def check_collisions(self, other_group):
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False
