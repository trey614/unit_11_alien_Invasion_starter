
class GameStats():
    
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.max_score = 0


    def reset_stats(self):
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self,collisions):
        self._update_score(collisions)

    def _update_max_score():
        if self.score > self.max_score:
            self.max_score = self.score


    def _update_score(self, collisions):
        
        for alien in collisions.values():
            self.score += self.settings.alien_points
    def update_level(self):
        self.level += 1
        print(self.level)

    


    
        



#Number of ships with have


