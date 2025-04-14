import sys
import pygame
from setting import Settings
from ship import Ship
from arsenal import ShipArsenal

# Main game class for Alien Invasion
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # Create the display screen
        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.running = True
        self.clock = pygame.time.Clock()

        # Initialize Arsenal and Ship objects
        self.arsenal = ShipArsenal(self)
        self.ship = Ship(self, self.arsenal)

        # Load and scale background image
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        # Initialize the sound system
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(str(self.settings.laser_sound))
        self.laser_sound.set_volume(0.7)

    def run_game(self):
        # Main game loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

            self._update_screen()

        pygame.quit()
        sys.exit()

    def _check_keydown_events(self, event):
        """Handle keydown events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()  # Play laser sound when firing
        elif event.key == pygame.K_q:
            self.running = False

    def _check_keyup_events(self, event):
        """Handle keyup events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update the screen by redrawing everything."""
        self.screen.blit(self.bg, (0, 0))
        self.ship.update()  # Update ship's movement
        self.ship.draw()  # Draw the ship
        self.arsenal.update_arsenal()  # Update arsenal (bullets)
        self.arsenal.draw()  # Draw bullets
        pygame.display.flip()  # Update the screen
        self.clock.tick(self.settings.FPS)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

