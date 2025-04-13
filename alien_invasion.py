import sys
import pygame
#Making an class for our alien invasion game, where we can set function to display screen.
class AlienInvasion:
    def __init__(self):
        pygame.init()
    #The __init__ is us inheriting from our imported classs
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.running = True
        #Here we are making our screen and setting its paremeter's
    def run_game(self):
        #Game Loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                    pygame.display.flip()
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    #We must set our class/ functions equal to someting so were able to run them.