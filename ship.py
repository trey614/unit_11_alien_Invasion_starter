import pygame
from typing import TYPE_CHECKING

# These imports are only used for type hints to avoid circular imports at runtime
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import ShipArsenal

class Ship:
    """A class to manage the player's ship."""

    def __init__(self, game: "AlienInvasion", arsenal: "ShipArsenal"):
        """
        Initialize the ship and its starting position.

        Args:
            game (AlienInvasion): The main game instance.
            arsenal (ShipArsenal): Object that manages bullets fired by the ship.
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        # Load the ship image, scale it, and rotate it to face right
        self.original_image = pygame.image.load(self.settings.ship_file)
        self.original_image = pygame.transform.scale(
            self.original_image, 
            (self.settings.ship_w, self.settings.ship_h)
        )
        self.image = pygame.transform.rotate(self.original_image, -90)

        # Get the image rectangle and set starting position
        self.rect = self.image.get_rect()
        self.rect.midleft = self.boundaries.midleft

        # Store float values for precise movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Arsenal object to manage bullets
        self.arsenal = arsenal

    def update(self):
        """
        Update the ship's position based on movement flags.
        Also updates the arsenal (e.g., bullets).
        """
        temp_speed = self.settings.ship_speed

        # Horizontal movement
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        # Vertical movement
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed

        # Apply updated positions
        self.rect.x = self.x
        self.rect.y = self.y

        # Update bullets
        self.arsenal.update_arsenal()

    def draw(self):
        """
        Draw the ship at its current location on the screen.
        """
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """
        Attempt to fire a bullet using the arsenal.

        Returns:
            bool: True if a bullet was fired, False otherwise.
        """
        return self.arsenal.fire_bullet()
