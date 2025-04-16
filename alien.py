import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    def __init__(self, game: 'AlienInvasion', x:float,y:float):
        super().__init__()
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.moving_right = False
        self.moving_left = False
        # Load the alien image and scale it based on settings
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image, 
            (self.settings.alien_w, self.settings.alien_h)
        )
   
        # Get the rectangle of the image and set its starting position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
       

        # Use a floating point for precise movement
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien up the screen."""
        temp_speed = self.settings.fleet_speed
        self.x -= temp_speed
        self.rect.x= self.x
       

    def draw_alien(self):
        
        self.screen.blit(self.image, self.rect)



