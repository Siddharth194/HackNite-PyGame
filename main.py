import pygame
from config import *
from basicfuncs import *
from LoadingScreen import *
from images import *

import os
import sys

WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption("HackNite Project")


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()

        self.rect = pygame.Rect(x,y,width,height)
        self.width = width
        self.height = height
        self.mask = None
        self.image = pygame.surface((width,height),pygame.SRCALPHA)

    def draw(self,WIN):

        WIN.blit(self.image, (self.rect.x,self.rect.y))

    def move_up(self):

        self.rect.y -= PLAYERVELOCITY
        self.direction = "up"

    def move_down(self):

        self.rect.y += PLAYERVELOCITY
        self.direction = "down"

    def move_left(self):

        self.rect.x -= PLAYERVELOCITY
        self.direction = "left"

    def move_right(self):

        self.rect.x += PLAYERVELOCITY
        self.direction = "right"    

def handlemovemenets(player):

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        player.move_right()
    
    if keys[pygame.K_a]:
        player.move_left()

    if keys[pygame.K_w]:
        player.move_up()
    
    if keys[pygame.K_s]:
        player.move_down()


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
    listindex = 0

    displayloadingscreen(WIN)

    while running:

        WIN.fill((255,255,255))
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if (listindex < 9*PLAYERSPEED):
            listindex += 1
        if listindex >= 44:
            listindex = 0

        WIN.blit(playerleft[listindex//PLAYERSPEED],(440,212))
            

        pygame.display.update()
    
    pygame.quit()

    
#if __name__ == "__main__":

main()
