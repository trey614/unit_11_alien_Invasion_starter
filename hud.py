import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class HUD:
    """
    Heads-Up Display (HUD) for showing score, high score, max score, level,
    and remaining lives (ships) in the Alien Invasion game.
    """

    def __init__(self, game: "AlienInvasion"):
        """
        Initialize HUD elements and prepare the images for display.

        Args:
            game (AlienInvasion): The main game instance.
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        self.font = pygame.font.Font(self.settings.font_file, self.settings.HUD_font_size)
        self.padding = 20

        self.update_scores()
        self._setup_life_image()
        self.update_level()

    def _setup_life_image(self):
        """Load and scale the ship image to represent player lives."""
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(
            self.life_image, (self.settings.ship_w, self.settings.ship_h)
        )
        self.life_rect = self.life_image.get_rect()

    def update_scores(self):
        """Update all score-related HUD elements."""
        self._update_score()
        self._update_hi_score()
        self._update_max_score()

    def _update_score(self):
        """Render the current score image and set its position."""
        score_str = f"Score: {self.game.game_stats.score:,.0f}"
        self.score_image = self.font.render(score_str, True, self.settings.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.padding

    def _update_max_score(self):
        """Render the max score image and set its position."""
        max_score_str = f"Max-Score: {self.game.game_stats.max_score:,.0f}"
        self.max_score_image = self.font.render(max_score_str, True, self.settings.text_color)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.score_rect.bottom + self.padding

    def _update_hi_score(self):
        """Render the high score image and center it at the top."""
        hi_score_str = f"Hi-Score: {self.game.game_stats.hi_score:,.0f}"
        self.hi_score_image = self.font.render(hi_score_str, True, self.settings.text_color)
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundaries.centerx, self.padding)
    
    def update_level(self):
        """Render the current level image and set its position."""
        level_str = f"Level: {self.game.game_stats.level}"
        self.level_image = self.font.render(level_str, True, self.settings.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.life_rect.bottom + self.padding

    def _draw_lives(self):
        """Draw remaining ships as life icons in the upper-left corner."""
        current_x = self.padding
        current_y = self.padding
        for _ in range(self.game.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding

    def draw(self):
        """Draw all HUD elements to the screen."""
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()
