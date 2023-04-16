import pygame
from config import * #long variable names written in caps are mostly imported from config
from basicfuncs import *
from LoadingScreen import *
from images import *
import random
import math


PLAYERVELOCITY = 3

WIN = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption("HackNite Project")
pygame.mixer.music.load("resources/Nightmare.mp3")
pygame.mixer.music.play(-1)


pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.rect = pygame.Rect(x,y,width+50,height)
        self.hprect=pygame.Rect(x,y,width//2,height//1.2)
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
        else:
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


        if self.hp//2 >= 3:
            imglist = rflist1
        elif self.hp//2 >= 2:
            imglist = rflist2
        elif self.hp//2 >= 1:
            imglist = rflist3
        else:
            imglist = rflist4

        if self.hp//2 < 1:
            self.maxdistortswitch = 0

            if self.maxdistortswitch == 0: 
                self.maxdistortswitch = 1
            else:
                self.maxdistortswitch = 0

            self.reflectedsprite = imglist[spriteindex][self.maxdistortswitch]
        
        elif self.hp//2 < 2:
            self.reflectedsprite = imglist[spriteindex][self.fightcount//FIGHTSPEED]

        else:
            self.reflectedsprite = imglist[spriteindex][self.fightcount//FIGHTSPEED]
        
        if count>0:
            self.reflectedsprite = imglist[spriteindex][0]

        return count

 
def activateenemy(player,enemy):
    dist = ((player.rect.x - enemy.rect.x)**2 + (player.rect.y - enemy.rect.y)**2)**0.5

    if dist <= 300:
        return True
    
    else:
        return False

def enemyattack(player,enemy):
    if activateenemy(player,enemy):
        return True
    else:
        return False


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
        self.velocity = ENEMYVELOCITY
        self.dead=False
        
        #self.offset = [0,0]

    def draw(self,WIN):        
        self.image.fill((0,0,0,0))
        self.image.blit(self.currentsprite,(0,0))
        WIN.blit(self.image, (self.rect.x,self.rect.y))
        
    
    def move_up(self):

        self.rect.y -= self.velocity
        self.direction = "up"

    def move_down(self):

        self.rect.y += self.velocity
        self.direction = "down"

    def move_left(self):

        self.rect.x -= self.velocity
        self.direction = "left"

    def move_right(self):

        self.rect.x += self.velocity
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

    def enemymovements(self,alert):

        if not self.dead:
        
            if not alert:
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

    def update_sprite_attack_enemy(self,ecount,angle):

        if angle >45 and angle <135:
            spriteindex = 0 #left
        elif angle <45 and angle>-45:
            spriteindex = 3 #up
        elif angle <-45 and angle >-135:
            spriteindex = 1
        else:
            spriteindex = 2
        
        if self.fightcount < 9*ENEMYSPEED-1:
            self.fightcount += 1
        else:
            self.fightcount = 0
        
        self.currentsprite = enemy_fightimgs[spriteindex][self.fightcount//ENEMYSPEED]

        if self.fightcount == 9*ENEMYSPEED - 1:
            ecount = 80
        
        if ecount > 0:
            self.currentsprite = enemy_fightimgs[spriteindex][0]

    def death(self):
        self.animationcount = 0
        if self.animationcount < 6*ENEMYSPEED - 1:
            self.animationcount += 1
        self.dead=True
        self.currentsprite = enemy_death[self.animationcount//ENEMYSPEED]

def handlemovements(player):

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
 
        if player.offset[0] >= -1810:
            player.move_right()
            player.offset[0] -= PLAYERVELOCITY

        return (1,True)
    
    if keys[pygame.K_a]:

        if player.offset[0] <= -3:
            player.move_left()
            player.offset[0] += PLAYERVELOCITY

        return (2,True)

    if keys[pygame.K_w]:

        if (-260+player.offset[1]) <= -240:
            player.move_up()
            player.offset[1] += PLAYERVELOCITY

        return (3,True)
    
    if keys[pygame.K_s]:

        if (-260+player.offset[1]) >= -850:
            player.move_down()
            player.offset[1] -= PLAYERVELOCITY

        return (4,True)
    
    return (0,False)


def drawscreen(player):
    WIN.blit(map,(player.offset[0],-260 + player.offset[1]))

def drawobject(player,object1):
    WIN.blit(object1.image, (object1.rect.x + player.offset[0],object1.rect.y + player.offset[1]))

def drawarrow(player,object1):
    WIN.blit(object1.image, (object1.rect.x,object1.rect.y))

def blitenemy(player,enemy):
    WIN.blit(enemy.image, (enemy.rect.x + player.offset[0],enemy.rect.y + player.offset[1]))

def handleattack(player,enemy_list):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        attack_check(player,enemy_list)
        return True
    
    return False

def attack_check(player,enemy_list):
    for enemy in enemy_list:
        if pygame.Rect.colliderect(enemy.rect,player.rect) and player.fightcount==5:
            enemy.hp-=1

def findangle(player,enemy):

    vectormag = ((player.rect.x-enemy.rect.x)**2 + ((player.rect.y+20) - enemy.rect.y)**2)**0.5
    enemyplayer = pygame.math.Vector2(player.rect.x - enemy.rect.x, (player.rect.y+20) - enemy.rect.y)
    arrowvector = pygame.math.Vector2(0,-1)
    
    cosine = (enemyplayer.dot(arrowvector))/vectormag
    angle = math.acos(cosine)

    if (player.rect.x - enemy.rect.x)>0:
        angle = -angle

    return int(angle*57.3)

'''
class Arrow(pygame.sprite.Sprite):
    def __init__(self,x,y,sprite):
        super.__init__()
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        self.rect = pygame.Rect(x,y,self.width,self.height)
        self.sprite = sprite
        self.image = pygame.Surface((self.width,self.height),pygame.SRCALPHA)
    
    def draw(self,WIN):

        self.image.fill((0,0,0,0))
        self.image.blit(self.sprite)'''

def arrowtravel(arrowobj,player,angle,initialpos):
    velx = -ARROWVELOCITY * math.sin(angle/57.3)
    vely = -ARROWVELOCITY * math.cos(angle/57.3)

    arrowobj.rect.x += velx + initialpos[0] - player.rect.x #- initialoffset[0] + player.offset[0] #velx
    arrowobj.rect.y += vely + initialpos[1] - player.rect.y#- initialoffset[1] + player.offset[1]

    arrowobj.draw(WIN)

    return arrowobj


class Object(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, sprite, name = None):
        super().__init__()

        self.rect = pygame.Rect(x,y,width,height)
        self.buildingrect = pygame.Rect(x+80,y+height//2,width-60,height//4)
        #self.hp_buildingrect = pygame.Rect(x+80,y+height//2,width,height//4)
        self.width = width
        self.height = height
        self.name = name
        self.currentsprite = sprite

        self.image = pygame.Surface((width,height),pygame.SRCALPHA)

    def draw(self,WIN):
        
        self.image.fill((0,0,0,0))
        self.image.blit(self.currentsprite,(0,0))
        WIN.blit(self.image, (self.rect.x,self.rect.y))
def health_pickup(player,health_pack,keypress):
    if health_pack.buildingrect.colliderect(player.rect):
    #if player.hprect.colliderect(health_pack.buildingrect):
        player.hp+=1
        return True
    return False
def collision(player,object1,keypress):
    if object1.buildingrect.colliderect(player.rect):
            if keypress[0] == 1:
                player.rect.right = object1.buildingrect.left
                player.offset[0] += PLAYERVELOCITY
            elif keypress[0] == 2:
                player.offset[0] -= PLAYERVELOCITY
                player.rect.left = object1.buildingrect.right
            elif keypress[0] == 3:
                player.rect.top = object1.buildingrect.bottom
                player.offset[1] -= PLAYERVELOCITY
            elif keypress[0] == 4:
                player.offset[1] += PLAYERVELOCITY
                player.rect.bottom = object1.buildingrect.top


def main():
    alert = []
    count = 0
    ecount = 0
    rotarrow = arrow
    arrowcd = 0
    counter=0
    

    random_health=[[(450,800),(230,842)],[(800,1560),(520,565)],[(800,1560),(812,840)]]
    health_packs=[]
    
    enemy_list=[]
    running = True
    clock = pygame.time.Clock()
    keypress = (2,False)

    player = Player(450,250,54,88)
    house = Object(900,150,432,415,House)
    hut = Object(1300,650,232,212,Hut)
    shop = Object(1500,250,692,317,Shop)

    for i in range(5):
        index=random.randint(0,2)
        p=random_health[index]
        rx=random.randint(p[0][0],p[0][1])
        ry=random.randint(p[1][0],p[1][1])
        healthobj=Object(rx,ry,100,100,Health)
        health_packs.append(healthobj)
    '''for health in health_packs:
        print(health.rect.x,health.rect.y)'''
    


    enemy_list.append(Enemy(random.randint(450,550),229,54,88,enemy_sprite))
    alert.append(False)
    enemy_list.append(Enemy(random.randint(450,900),530,54,88,enemy_sprite))
    alert.append(False)
    enemy_list.append(Enemy(random.randint(1750,1950),530,54,88,enemy_sprite))
    alert.append(False)

    arrowobj = Object(enemy_list[0].rect.x,enemy_list[0].rect.y,rotarrow.get_width(),rotarrow.get_height(),rotarrow)
    angle = findangle(player,enemy_list[0])
    
    def ysort(player,house,shop,hut,healthlist):
        
        check = 0
        
        objectlist = [house,shop,hut]
        for i in healthlist:
            objectlist.append(i)
        for i in range(len(objectlist)):
            if objectlist[i].rect.centery >= player.rect.centery:
                objectlist.insert(i,player)
                check = 1

        if not check:
            objectlist.append(player)
            
        return objectlist

    while running:


        arrowcheck = 0

        initialpos = (player.rect.x,player.rect.y)

        house.draw(WIN)
        hut.draw(WIN)
        shop.draw(WIN)
        for health in health_packs:
            health.draw(WIN)


        WIN.fill((255,255,255))
        clock.tick(FPS)

        for enemy in enemy_list:
            enemy.draw(WIN)

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        collision(player,house,keypress)
        collision(player,hut,keypress)
        collision(player,shop,keypress)
        '''collision(player,health_packs[0],keypress)
        collision(player,health_packs[1],keypress)
        collision(player,health_packs[2],keypress)
        collision(player,health_packs[3],keypress)
        collision(player,health_packs[4],keypress)'''

        for health_pack in health_packs:
            if health_pickup(player,health_pack,keypress):
                health_packs.remove(health_pack)

        keypress = handlemovements(player)
        
        player.update_sprite(keypress[1])

        if not keypress[1]:
            keypress2 = handleattack(player,enemy_list)
            count = player.update_sprite_attack(keypress2,count)

        drawscreen(player)

        objectlist = ysort(player,house,shop,hut,health_packs)
        #objectlist = ysort(player,house,shop,hut,health_packs)

        for i in objectlist:

            if i == player:
                player.draw(WIN)
            else:  
                drawobject(player,i)

        for e in range(len(enemy_list)):
            blitenemy(player,enemy_list[e])
            enemy_list[e].enemymovements(alert[e])
            #if not enemy_list[e].dead:
            alert[e] = enemyattack(player,enemy_list[e])

        for i in range(len(enemy_list)):
            if enemy_list[i].dead==False:
                alert[i] = enemyattack(player,enemy_list[i])
                if alert[i]:
                    rotarrow = pygame.transform.rotate(arrow,angle)
                    enemy_list[i].update_sprite_attack_enemy(ecount,angle)
                    
                    if arrowcd == 0:
                        arrowobj = Object(enemy_list[i].rect.x + player.offset[0],enemy_list[i].rect.y + player.offset[1],pygame.transform.rotate(arrow,angle).get_width(),pygame.transform.rotate(arrow,angle).get_height(),pygame.transform.rotate(arrow,angle))
                        arrowcd = 200
                        angle = findangle(player,enemy_list[i])
                        arrowtravel(arrowobj,player,angle,initialpos)
                    else:
                        arrowcd -= 1
                        arrowtravel(arrowobj,player,angle,initialpos)
                    
                    if arrowobj.rect.colliderect(player.rect):
                        player.hp -= 0.001
                        arrowcheck = 1
        
        print(player.hp)
        if not arrowcheck:
            player.hp = int(player.hp)

        
        #alive_enemies=[]
        if len(enemy_list)!=0:
            
            for enemy in enemy_list:
                    if enemy.dead==True:
                        enemy.currentsprite = enemy_death[5]
                        #enemy.draw(WIN)
                        blitenemy(player,enemy)
                    else:
                        if enemy.hp<=0:
                            enemy.death()
                            #blitenemy(player,enemy)

                            '''blitenemy(player,enemy)
                            enemy.enemymovements(alert)'''
                    #alive_enemies.append(i)
                        else:
                            blitenemy(player,enemy)
                            enemy.enemymovements(alert)
                            

        #temp=[]
        '''for i in alive_enemies:
            temp.append(enemy_list[i])
        enemy_list=temp'''

        #print(player.rect.x,player.rect.y)
        count-=1
        
        


        pygame.display.update()
    
    pygame.quit()


displayloadingscreen(WIN)
displaymenuscreen(WIN)
main()

