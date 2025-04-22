from pathlib import Path
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats:
    """Track and manage statistics for the Alien Invasion game."""

    def __init__(self, game):
        """
        Initialize statistics and load high scores from file.

        Args:
            game (AlienInvasion): The main game instance.
        """
        self.game = game
        self.settings = game.settings
        self.path = self.settings.scores_file

        self.max_score = 0      # Highest score during current play session
        self.init_saved_scores()
        self.reset_stats()      # Initialize game state variables

    def init_saved_scores(self):
        """
        Load the saved high score from a JSON file.
        If the file is missing or invalid, initialize a score of 0.
        """
        if self.path.exists() and self.path.stat().st_size > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get("hi_score", 0)
        else:
            self.hi_score = 0
            self.save_scores()  # Create the file if it doesn't exist

    def save_scores(self):
        """
        Save the current high score to the JSON file.
        """
        scores = {"hi_score": self.hi_score}
        contents = json.dumps(scores, indent=4)

        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f"File Not Found: {e}")

    def reset_stats(self):
        """
        Reset the game's statistics to their starting values.
        Called at the beginning of a game or when restarting.
        """
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        """
        Update the score, max score, and high score based on collisions.

        Args:
            collisions (dict): Result of `pygame.sprite.groupcollide()`
        """
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_score(self, collisions):
        """
        Increase score for each alien hit in collisions.

        Args:
            collisions (dict): Result of group collision detection.
        """
        for aliens_hit in collisions.values():
            self.score += self.settings.alien_points * len(aliens_hit)

    def _update_max_score(self):
        """Update session max score if the current score exceeds it."""
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_hi_score(self):
        """Update high score if the current score exceeds the saved score."""
        if self.score > self.hi_score:
            self.hi_score = self.score

    def update_level(self):
        """Increase the level after defeating a wave of aliens."""
        self.level += 1
