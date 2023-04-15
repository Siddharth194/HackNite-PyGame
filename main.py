import pygame
from config import * #long variable names written in caps are mostly imported from config
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
        self.direction = "front"
        self.mask = None
        self.image = pygame.Surface((width,height*2),pygame.SRCALPHA)
        self.animationcount = 0
        self.hp = 1

    def draw(self,WIN):
        
        self.image.fill((0,0,0,0))
        self.image.blit(self.currentsprite,(0,0))
        self.image.blit(self.reflectedsprite,(0,self.height))
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
        
    def update_sprite(self,keypress):

        if self.direction == "up":
            spriteindex = 3
        elif self.direction == "down":
            spriteindex = 2
        elif self.direction == "left":
            spriteindex = 0
        else:
            spriteindex = 1
        
        if keypress:
            if self.animationcount < 9*PLAYERSPEED - 1:
                self.animationcount += 1
            else:
                self.animationcount = 0

        self.currentsprite = movementimgs[spriteindex][self.animationcount//PLAYERSPEED]


        #from here, handling the reflection sprites
        if self.hp//2 >= 3:
            imglist = refld1
        elif self.hp//2 >= 2:
            imglist = refld2
        elif self.hp//2 >= 1:
            imglist = refld3
        elif self.hp//2 >= 0:
            imglist = refld4
        
        if self.hp//2 < 1:
            self.maxdistortswitch = 0
            if self.maxdistortswitch == 0:
                self.maxdistortswitch = 1
            else:
                self.maxdistortswitch = 0

            self.reflectedsprite = imglist[spriteindex][self.maxdistortswitch]
        
        elif self.hp//2 < 2:
            self.reflectedsprite = imglist[spriteindex][self.animationcount//PLAYERSPEED]

        else:
            self.reflectedsprite = imglist[spriteindex][self.animationcount//PLAYERSPEED]



def handlemovements(player):

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        player.move_right()
        return True
    
    if keys[pygame.K_a]:
        player.move_left()
        return True

    if keys[pygame.K_w]:
        player.move_up()
        return True
    
    if keys[pygame.K_s]:
        player.move_down()
        return True
    
    return False


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

    player = Player(450,250,54,88)

    while running:

        WIN.fill((255,255,255))
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        '''if (listindex < 9*PLAYERSPEED):
            listindex += 1
        if listindex >= 44:
            listindex = 0

        WIN.blit(playerleft[listindex//PLAYERSPEED],(440,212))'''
        
        keypress = handlemovements(player)
        player.update_sprite(keypress)
        player.draw(WIN)

    
        
        pygame.display.update()
    
    pygame.quit()

    
#if __name__ == "__main__":

main()
