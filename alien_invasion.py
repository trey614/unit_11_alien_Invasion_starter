import sys
import pygame
from setting import Settings
from ship import Ship
from arsenal import ShipArsenal
from alien import Alien

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # Create the display screen
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        self.running = True
        self.clock = pygame.time.Clock()

        # Initialize Arsenal and Ship objects
        self.arsenal = ShipArsenal(self)
        self.ship = Ship(self, self.arsenal)

        # Initialize Alien Group and add at least one alien
        self.aliens = pygame.sprite.Group()
        alien = Alien(self, 800, 100)  # You can customize position
        self.aliens.add(alien)

        # Load and scale background image
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg, (self.settings.screen_w, self.settings.screen_h)
        )

        # Initialize the sound system
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(str(self.settings.laser_sound))
        self.laser_sound.set_volume(0.7)

    def run_game(self):
        """Main game loop."""
        while self.running:
            self._check_events()
            self.ship.update()
            self.arsenal.update_arsenal()
            self.aliens.update()  # Update all aliens
            self._update_screen()

        pygame.quit()
        sys.exit()

    def _check_events(self):
        """Check for events like key presses and quitting."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
      
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
        elif event.key == pygame.K_q:
            self.running = False

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        """Redraw all game elements on the screen."""
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.arsenal.draw()
        self.aliens.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(self.settings.FPS)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
