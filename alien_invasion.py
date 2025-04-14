import sys
import pygame
from setting import Settings
from ship import Ship

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
        self.ship = Ship(self)

        # Load and scale background image
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

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
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.running = False

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))
        self.ship.update()
        self.ship.draw()
        pygame.display.flip()
        self.clock.tick(self.settings.FPS)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
