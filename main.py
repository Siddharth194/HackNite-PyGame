import pygame
from config import * #long variable names written in caps are mostly imported from config
from basicfuncs import *
from LoadingScreen import *
from images import *

import os
import sys

PLAYERVELOCITY = 3

WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption("HackNite Project")

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.rect = pygame.Rect(x,y,width+50,height)
        self.width = width
        self.height = height
        self.direction = "down"
        self.mask = None
        self.image = pygame.Surface((width+50,height*2),pygame.SRCALPHA)
        self.animationcount = 0
        self.fightcount=0
        self.hp = 7

        self.offset = [0,0]

    def draw(self,WIN):
        
        self.image.fill((0,0,0,0))
        self.image.blit(self.currentsprite,(0,0))
        self.image.blit(self.reflectedsprite,(0,self.height-5))
        #WIN.blit(self.image, (self.rect.x,self.rect.y))
        WIN.blit(self.image, (423,256))

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
        

        self.reflectedsprite = pygame.transform.scale(self.reflectedsprite,(54,70))
    
    def update_sprite_attack(self,keypress,count):

        if self.direction == "up":
            spriteindex = 3
        elif self.direction == "down":
            spriteindex = 2
        elif self.direction == "left":
            spriteindex = 0
        else:
            spriteindex = 1
        
        if keypress:
            if self.fightcount < 6*FIGHTSPEED - 1:
                self.fightcount += 1
            else:
                self.fightcount = 0
            
            self.currentsprite = fightimgs[spriteindex][self.fightcount//FIGHTSPEED]

            if self.fightcount//FIGHTSPEED == 5:
                count=20
            if count>0:
                self.currentsprite = fightimgs[spriteindex][0]

        return count

def handlemovements(player):

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        player.move_right()
 
        if player.offset[0] >= -1810:
            player.offset[0] -= PLAYERVELOCITY

        return (1,True)
    
    if keys[pygame.K_a]:
        player.move_left()

        if player.offset[0] <= -3:
            player.offset[0] += PLAYERVELOCITY

        return (2,True)

    if keys[pygame.K_w]:
        player.move_up()

        if (-260+player.offset[1]) <= -250:
            player.offset[1] += PLAYERVELOCITY

        return (3,True)
    
    if keys[pygame.K_s]:
        player.move_down()

        if (-260+player.offset[1]) >= -850:
            player.offset[1] -= PLAYERVELOCITY

        return (4,True)
    
    return (0,False)


def drawscreen(player):
    WIN.blit(map,(player.offset[0],-260 + player.offset[1]))

def drawobject(player,object1,keypress):

    #print(object1.rect.x + player.offset[0],object1.rect.y + player.offset[1])
    WIN.blit(object1.image, (object1.rect.x + player.offset[0],object1.rect.y + player.offset[1]))


def handleattack(player):

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        return True
    
    return False

class Object(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, sprite, name = None):
        super().__init__()

        self.rect = pygame.Rect(x,y,width,height)
        self.buildingrect = pygame.Rect(x+60,y+height//2,width,height//4)
        self.width = width
        self.height = height
        self.name = name
        self.currentsprite = sprite

        self.image = pygame.Surface((width,height),pygame.SRCALPHA)

    def draw(self,WIN):
        
        self.image.fill((0,0,0,0))
        self.image.blit(self.currentsprite,(0,0))
        #WIN.blit(self.image, (self.rect.x,self.rect.y))
        WIN.blit(self.image, (self.rect.x,self.rect.y))


def main():
    count = 0
    pygame.mixer.music.load("resources/Nightmare.mp3")
    pygame.mixer.music.play(-1)

    running = True
    clock = pygame.time.Clock()
    listindex = 0

    #displayloadingscreen(WIN)

    player = Player(450,250,54,88)
    house = Object(900,150,432,415,House)
    hut = Object(1300,650,232,212,Hut)
    shop = Object(1500,250,692,317,Shop)

    def ysort(player,house,shop,hut):
        
        check = 0
        objectlist = [house,shop,hut]
        for i in range(len(objectlist)):
            if objectlist[i].rect.centery >= player.rect.centery:
                objectlist.insert(i,player)
                check = 1

        if not check:
            objectlist.append(player)
            
        return objectlist

    while running:
 
        house.draw(WIN)
        hut.draw(WIN)
        shop.draw(WIN)

        WIN.fill((255,255,255))
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if house.buildingrect.colliderect(player.rect):
            if keypress[0] == 1:
                player.rect.right = house.buildingrect.left
                player.offset[0] += PLAYERVELOCITY
            elif keypress[0] == 2:
                player.offset[0] -= PLAYERVELOCITY
                player.rect.left = house.buildingrect.right
            elif keypress[0] == 3:
                player.rect.top = house.buildingrect.bottom
                player.offset[1] -= PLAYERVELOCITY
            elif keypress[0] == 4:
                player.offset[1] += PLAYERVELOCITY
                player.rect.bottom = house.buildingrect.top
        
        if hut.buildingrect.colliderect(player.rect):
            if keypress[0] == 1:
                player.rect.right = hut.buildingrect.left
                player.offset[0] += PLAYERVELOCITY
            elif keypress[0] == 2:
                player.offset[0] -= PLAYERVELOCITY
                player.rect.left = hut.buildingrect.right
            elif keypress[0] == 3:
                player.rect.top = hut.buildingrect.bottom
                player.offset[1] -= PLAYERVELOCITY
            elif keypress[0] == 4:
                player.offset[1] += PLAYERVELOCITY
                player.rect.bottom = hut.buildingrect.top
        
        if shop.buildingrect.colliderect(player.rect):
            if keypress[0] == 1:
                player.rect.right = shop.buildingrect.left
                player.offset[0] += PLAYERVELOCITY
            elif keypress[0] == 2:
                player.offset[0] -= PLAYERVELOCITY
                player.rect.left = shop.buildingrect.right
            elif keypress[0] == 3:
                player.rect.top = shop.buildingrect.bottom
                player.offset[1] -= PLAYERVELOCITY
            elif keypress[0] == 4:
                player.offset[1] += PLAYERVELOCITY
                player.rect.bottom = shop.buildingrect.top

        keypress = handlemovements(player)
        
        player.update_sprite(keypress[1])

        if not keypress[1]:
            keypress2 = handleattack(player)
            count = player.update_sprite_attack(keypress2,count)

        drawscreen(player)

        objectlist = ysort(player,house,shop,hut)

        for i in objectlist:

            if i == player:
                player.draw(WIN)
            else:
                drawobject(player,i,keypress)

        count -= 1
        pygame.display.update()
    
    pygame.quit()

main()
