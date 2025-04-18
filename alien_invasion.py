import sys
import pygame
from setting import Settings
from ship import Ship
from game_stats import GameStats
from arsenal import ShipArsenal
from alien_fleet import AlienFleet
from time import sleep

class AlienInvasion:
    def __init__(self):
        # Initialize Pygame and game settings
        pygame.init()
        self.settings = Settings()
        self.game_stats = GameStats(self.settings.starting_ship_count)

        # Set up the game window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        self.running = True
        self.clock = pygame.time.Clock()

        # Create player's arsenal (bullets) and ship
        self.arsenal = ShipArsenal(self)
        self.ship = Ship(self, self.arsenal)

        # Create the alien fleet
        self.alien_fleet = AlienFleet(self)

        # Load and scale the background image
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg, (self.settings.screen_w, self.settings.screen_h)
        )

        # Initialize mixer and load sound effects
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(str(self.settings.laser_sound))
        self.laser_sound.set_volume(0.7)

        self.impact_sound_bullet = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound_bullet.set_volume(0.7)

        self.impact_sound_ship = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound_ship.set_volume(0.7)

        # Game state flag
        self.game_active = True

    def run_game(self):
        """Main game loop that runs while the game is active."""
        while self.running:
            self._check_events()  # Handle player input

            if self.game_active:
                self.ship.update()  # Update ship movement
                self.alien_fleet.update_fleet()  # Update alien fleet movement
                self._check_collisions()  # Handle collisions

            self.arsenal.update_arsenal()  # Update bullet positions
            self._update_screen()  # Redraw everything on the screen

        pygame.quit()
        sys.exit()

    def _check_collisions(self):
        """Handle all game collision logic."""
        # If aliens reach the left side, check game state
        if self.alien_fleet.check_fleet_left():
            self._check_game_status()

        # Detect bullet-alien collisions and remove both
        collisions = pygame.sprite.groupcollide(
            self.arsenal.arsenal, self.alien_fleet.fleet, True, True
        )
        if collisions:
            self.impact_sound_bullet.play()

        # Detect ship-alien collisions
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self.impact_sound_ship.play()
            self._check_game_status()

        # Reset level if any alien reaches the left screen edge
        for alien in self.alien_fleet.fleet:
            if alien.rect.left <= 0:
                self._reset_level()
                break

        # If all aliens are destroyed, start a new wave
        if self.alien_fleet.check_destroyed_status():
            self._reset_level()

    def _check_game_status(self):
        """Check if player has remaining lives or end game."""
        if self.game_stats.ship_limit > 1:
            self.game_stats.ship_limit -= 1  # Decrease remaining lives
            self._reset_level()
            sleep(0.5)  # Short pause before new level
        else:
            self.game_active = False  # End the game

    def _reset_level(self):
        """Reset bullets and aliens when the player gets hit or aliens break through."""
        self.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()
        self.ship._center_ship()

    def _check_events(self):
        """Listen for keyboard and mouse input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Handle keydown events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():  # Fire a bullet if allowed
                self.laser_sound.play()
        elif event.key == pygame.K_q:
            self.running = False  # Quit the game

    def _check_keyup_events(self, event):
        """Handle keyup events."""
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
        self.screen.blit(self.bg, (0, 0))  # Draw background
        self.ship.draw()  # Draw player ship
        self.arsenal.draw()  # Draw bullets
        self.alien_fleet.draw()  # Draw aliens
        pygame.display.flip()  # Flip to updated display
        self.clock.tick(self.settings.FPS)  # Maintain frame rate

# Run the game
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
