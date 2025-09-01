import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    game_over = False
    while game_over != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Fills the background
        pygame.Surface.fill(screen, (0, 0, 0))
        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")
        #Refreshes the screen
        pygame.display.flip()
        dt = clock.tick(60)/1000

        

if __name__ == "__main__":
    main()
