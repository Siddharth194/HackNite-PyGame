import pygame
from config import * #long variable names written in caps are mostly imported from config
from basicfuncs import *
from LoadingScreen import *
from images import *

import os
import sys
import random


WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption("HackNite Project")

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.rect = pygame.Rect(x,y,width+50,height)
        self.width = width
        self.height = height
        self.direction = "front"
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
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height,sprite):
        super().__init__()

        self.X=x
        self.Y=y
        self.rect = pygame.Rect(x,y,width+50,height)
        self.width = width
        self.height = height
        self.direction = "right"
        self.mask = None
        self.image = pygame.Surface((width+50,height),pygame.SRCALPHA)
        self.animationcount = 0
        self.fightcount=0
        self.hp = 3
        self.currentsprite = sprite
        
        #self.offset = [0,0]

    def draw(self,WIN):        
        self.image.fill((0,0,0,0))
        self.image.blit(self.currentsprite,(0,0))
        WIN.blit(self.image, (self.rect.x,self.rect.y))
    
    def move_up(self):

        self.rect.y -= ENEMYVELOCITY
        self.direction = "up"

    def move_down(self):

        self.rect.y += ENEMYVELOCITY
        self.direction = "down"

    def move_left(self):

        self.rect.x -= ENEMYVELOCITY
        self.direction = "left"

    def move_right(self):

        self.rect.x += ENEMYVELOCITY
        self.direction = "right"
    
    def update_sprite(self):

        if self.direction == "up":
            enemy_spriteindex = 3
        elif self.direction == "down":
            enemy_spriteindex = 2
        elif self.direction == "left":
            enemy_spriteindex = 0
        else:
            enemy_spriteindex = 1
        
        
        if self.animationcount < 9*ENEMYSPEED - 1:
            self.animationcount += 1
        else:
            self.animationcount = 0

        self.currentsprite = enemy_movementimgs[enemy_spriteindex][self.animationcount//ENEMYSPEED]

    def enemymovements(self):
        if self.direction=="right":
            if self.rect.x>=self.X and self.rect.x<(self.X+SIDE):
                self.move_right()
                self.update_sprite()
            else:
                self.direction="down"
                self.update_sprite()
            
        elif self.direction=="down":
            if self.rect.y>=self.Y and self.rect.y<(self.Y+SIDE):
                self.move_down()
                self.update_sprite()
            else:
                self.direction="left"
                self.update_sprite()
        elif self.direction=="left":
            if self.rect.x>self.X and self.rect.x<=(self.X+SIDE):
                self.move_left()
                self.update_sprite()
            else:
                self.direction="up"
                self.update_sprite()
        else:
            if self.rect.y<=(self.Y+SIDE) and self.rect.y>self.Y:
                self.move_up()
                self.update_sprite()
            else:
                self.direction="right"
                self.update_sprite()

def handlemovements(player):

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        player.move_right()
 
        if player.offset[0] >= -1810:
            player.offset[0] -= PLAYERVELOCITY

        return True
    
    if keys[pygame.K_a]:
        player.move_left()

        if player.offset[0] <= -3:
            player.offset[0] += PLAYERVELOCITY

        return True

    if keys[pygame.K_w]:
        player.move_up()

        if (-260+player.offset[1]) <= -250:
            player.offset[1] += PLAYERVELOCITY

        return True
    
    if keys[pygame.K_s]:
        player.move_down()

        if (-260+player.offset[1]) >= -850:
            player.offset[1] -= PLAYERVELOCITY

        return True
    
    return False



def handleattack(player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP_ENTER]:
        return True
    return False
def drawscreen(player):
    WIN.blit(map,(player.offset[0],-260 + player.offset[1]))


def blitenemy(player,enemy):

    WIN.blit(enemy.image, (enemy.rect.x + player.offset[0],enemy.rect.y + player.offset[1]))

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
    count=0
    counter=0
    pygame.mixer.music.load("resources/Nightmare.mp3")
    pygame.mixer.music.play(-1)

    running = True
    clock = pygame.time.Clock()
    listindex = 0
    enemy_list=[]
    displayloadingscreen(WIN)

    player = Player(450,250,54,88)
    #enemy=Enemy(500,250,54,88,enemy_sprite)

    while running:
        #enemy.draw(WIN)
        for enemy in enemy_list:
            enemy.draw(WIN)
        #WIN.fill((255,255,255))
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        '''if (listindex < 9*PLAYERSPEED):
            listindex += 1
        if listindex >= 44:
            listindex = 0

        WIN.blit(playerleft[listindex//PLAYERSPEED],(440,212))'''
        
        keypress1 = handlemovements(player)
        player.update_sprite(keypress1)
        if not keypress1:
            keypress2=handleattack(player)
            count=player.update_sprite_attack(keypress2,count)
        drawscreen(player)
        player.draw(WIN)
        
        if counter%100==0:
            rx=random.randint(0,900)
            ry=random.randint(0,600)
            enemy=Enemy(rx,ry,54,88,enemy_sprite)
            enemy_list.append(enemy)

        for enemy in enemy_list:
            #enemy.draw(WIN)
            blitenemy(player,enemy)
            enemy.enemymovements()
        #blitenemy(player,enemy)
        #enemy.enemymovements()
        #enemy.update_sprite()
        count=count-1
        counter+=1
        pygame.display.update()
    pygame.quit()

    
#if __name__ == "__main__":

main()
