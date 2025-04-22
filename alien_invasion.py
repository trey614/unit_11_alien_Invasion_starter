import sys
import pygame
from setting import Settings
from ship import Ship
from game_stats import GameStats
from arsenal import ShipArsenal
from alien_fleet import AlienFleet
from time import sleep
from button import Button
from hud import HUD

class AlienInvasion:
    """Main class to manage game behavior and assets."""

    def __init__(self):
        """Initialize the game, settings, screen, and assets."""
        pygame.init()
        self.settings = Settings()
        self.game_stats = GameStats(self)
        self.settings.initialize_dynamic_settings()

        # Set up game screen
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        # Game-related objects
        self.HUD = HUD(self)
        self.clock = pygame.time.Clock()
        self.running = True

        # Game components
        self.arsenal = ShipArsenal(self)     # Manages bullets
        self.ship = Ship(self, self.arsenal) # Player's ship
        self.alien_fleet = AlienFleet(self)  # Manages all alien sprites

        # Background image
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        # Initialize sound effects
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(str(self.settings.laser_sound))
        self.laser_sound.set_volume(0.7)
        self.impact_sound_bullet = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound_bullet.set_volume(0.7)
        self.impact_sound_ship = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound_ship.set_volume(0.7)

        # UI elements
        self.play_button = Button(self, "Play")
        self.game_active = False  # Starts in inactive state until Play is clicked

    def run_game(self):
        """Main loop that keeps the game running."""
        while self.running:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()

            self.arsenal.update_arsenal()
            self._update_screen()

        pygame.quit()
        sys.exit()

    def _check_collisions(self):
        """Detect and respond to collisions between entities."""
        
        # Check if aliens reached the left edge
        if self.alien_fleet.check_fleet_left():
            self._check_game_status()

        # Check bullet-alien collisions
        collisions = pygame.sprite.groupcollide(
            self.arsenal.arsenal, self.alien_fleet.fleet, True, True
        )
        if collisions:
            self.impact_sound_bullet.play()

        # Check ship-alien collisions
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self.impact_sound_ship.play()
            self._check_game_status()
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        # If an alien reaches the screen's left side
        for alien in self.alien_fleet.fleet:
            if alien.rect.left <= 0:
                self._reset_level()
                break

        # If all aliens are destroyed, start a new wave
        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            self.game_stats.update_level()
            self.HUD.update_level()

        # Add score from hit aliens
        for aliens_hit in collisions.values():
            self.game_stats.score += self.settings.alien_points * len(aliens_hit)
        self.HUD.update_scores()

    def _check_game_status(self):
        """Check if player has remaining lives; end game if not."""
        if self.game_stats.ships_left > 1:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

    def _reset_level(self):
        """Clear all bullets/aliens and reset ship and alien fleet."""
        self.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()
        self.ship._center_ship()

    def restart_game(self):
        """Reset everything and restart the game after 'Play' is clicked."""
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)
        self.HUD.update_scores()

    def _check_events(self):
        """Respond to key and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.game_stats.save_scores()
            elif event.type == pygame.KEYDOWN and self.game_active:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        """Start a new game if the play button is clicked."""
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()

    def _check_keydown_events(self, event):
        """Handle key presses."""
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
            self.game_stats.save_scores()

    def _check_keyup_events(self, event):
        """Handle key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        """Redraw all game elements and update the screen."""
        self.screen.blit(self.bg, (0, 0))  # Draw background
        self.ship.draw()
        self.arsenal.draw()
        self.alien_fleet.draw()
        self.HUD.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()
        self.clock.tick(self.settings.FPS)

# Run the game if script is executed directly
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
