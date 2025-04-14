import sys
import pygame
from setting import Settings
#Making an class for our alien invasion game, where we can set function to display screen.
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
    #The __init__ is us inheriting from our imported classs
        self.screen = pygame.display.set_mode((self.settings.screen_w,self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)
        self.running = True
        #Here we are making our screen and setting its paremeter's
        self.clock = pygame.time.Clock()
    def run_game(self):
        #Game Loop
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
            self.screen.blit(self.bg, (0,0))
            pygame.display.flip()
            self.clock.tick(self.settings.FPS)
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    #We must set our class/ functions equal to someting so were able to run them.