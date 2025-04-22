from pathlib import Path
import json
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvaion
class GameStats():
    
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()
        self.path = self.settings.scores_file
    
        

    def init_saved_scores(self):
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat().st_size > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get("hi_score", 0)
        else:
            self.hi_score = 0
            self.save_scores()


    def _update_hi_score(self):
        if self.score > self.hi_score:
            self.hi_score = self.score
    
    def save_scores(self):
        scores = {"hi_score": self.hi_score}

        contents = json.dumps(scores, indent=4)
        try:

            self.path.write_text(contents)
        except FileNotfoundError as e:
            print(f"Finle Not Found: {e}")


            


    def reset_stats(self):
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self,collisions):
        self._update_score(collisions)

        self._update_max_score()


        self._update_hi_score()

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score


    def _update_score(self, collisions):
        
        for alien in collisions.values():
            self.score += self.settings.alien_points
    def update_level(self):
        self.level += 1
        #print(self.level)

    


    
        



#Number of ships with have


