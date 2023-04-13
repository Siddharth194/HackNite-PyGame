import pygame
from config import * 
import os

#pygame.init()

WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

'''def draw_window():
    WIN.fill'''


def main():
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.display.update()
    pygame.quit()
if __name__ == "__main__":
    main()