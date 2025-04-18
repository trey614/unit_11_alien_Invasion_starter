import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

# Prevent circular imports during runtime
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion 

class ShipArsenal:
    """Manages all bullets fired by the player's ship."""
    
    def __init__(self, game: "AlienInvasion"):
        """
        Initialize the arsenal.

        Args:
            game (AlienInvasion): The main game instance for accessing settings and screen.
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.arsenal = pygame.sprite.Group()  # Group to hold all bullets

    def update_arsenal(self):
        """Update the position of bullets and remove offscreen ones."""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """Remove bullets that have moved beyond the right edge of the screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.left > self.boundaries.right:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draw all bullets in the arsenal on the screen."""
        for bullet in self.arsenal:
            bullet.draw_bullet()  # Assumes Bullet class has a draw_bullet method

    def fire_bullet(self):
        """
        Fire a new bullet if under the allowed bullet limit.

        Returns:
            bool: True if a bullet was fired, False if the limit was reached.
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)  
            return True
        return False
