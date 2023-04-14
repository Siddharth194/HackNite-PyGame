import pygame
from config import *
from basicfuncs import *
import os

WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

pygame.display.set_caption("HackNite Project")

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.rect = pygame.Rect(x,y,width,height)
        self.width = width
        self.height = height

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name = None):
        super().__init__()

        self.rect = pygame.Rect(x,y,width,height)
        self.width = width
        self.height = height
        self.name = name

        self.image = pygame.surface((width,height),pygame.SRCALPHA)

    def draw(self,WIN):

        WIN.blit(self.image, (self.rect.x,self.rect.y))


def main():
    running = True
    clock = pygame.time.Clock()

    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.display.update()
    pygame.quit()

    
if __name__ == "__main__":
    main()