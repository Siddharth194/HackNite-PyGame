import pygame
from basicfuncs import *
from config import *

pygame.init()

def im(dest):
    return pygame.image.load(dest)

WIN = pygame.display.set_mode((900,600))

loadingscreen = im('resources/LoadingScreen.png')

lslist = [im('resources/loadingscreen/1.png'),im('resources/loadingscreen/2.png'),im('resources/loadingscreen/3.png'),im('resources/loadingscreen/4.png'),im('resources/loadingscreen/5.png'),im('resources/loadingscreen/6.png'),im('resources/loadingscreen/7.png'),im('resources/loadingscreen/8.png'),im('resources/loadingscreen/9.png'),im('resources/loadingscreen/10.png'),im('resources/loadingscreen/11.png'),im('resources/loadingscreen/12.png'),im('resources/loadingscreen/13.png'),im('resources/loadingscreen/14.png'),im('resources/loadingscreen/15.png'),im('resources/loadingscreen/16.png'),im('resources/loadingscreen/17.png'),im('resources/loadingscreen/18.png'),im('resources/loadingscreen/19.png'),im('resources/loadingscreen/20.png'),im('resources/loadingscreen/21.png'),im('resources/loadingscreen/22.png'),im('resources/loadingscreen/23.png'),im('resources/loadingscreen/24.png'),im('resources/loadingscreen/25.png'),im('resources/loadingscreen/26.png'),im('resources/loadingscreen/27.png'),im('resources/loadingscreen/28.png'),im('resources/loadingscreen/29.png')]

def displayloadingscreen(WIN):

    running = True
    state = 0
    i = 0
    cycles = 0
    opacity = 0
    doneload = 0
    textfademultiplier = 1

    while running:
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        WIN.fill((0,0,0))

        if cycles == LOADINGSCREENDELAY:
            cycles = 0
            state = 1
            WIN.blit(loadingscreen,(0,0))
            pygame.display.update()
            #pygame.time.wait(2000)
            loadcheck = 1

        if state == 0:
            if i == 28*LOADINGSCREENSPEED:
                i = 0
                cycles += 1
            else:
                i = i + 1
            
            WIN.blit(lslist[i//30],(0,0))
        
        if state == 1:

            if opacity < 200 and not doneload:
                opacity += 2.5
            else:
                doneload = 1

            if doneload:
                templist = faderepeat(opacity,1,200,100,textfademultiplier)
                opacity = templist[0]
                textfademultiplier = templist[1]

            Donefont = pygame.font.Font('resources/fonts/RedHatText-Medium.ttf', 100)
            Donefont1 = Donefont.render("DONE", True, (178,161,223))
            Donefont1.set_alpha(int(opacity))

            startfont = pygame.font.Font('resources/fonts/RedHatText-Medium.ttf',30)
            startfont1 = startfont.render("Loading completed. Press any key to proceed.",True, (178,161,223))

            WIN.blit(loadingscreen,(0,0))
            WIN.blit(Donefont1,(310,220))
            WIN.blit(startfont1, (120,360))


        pygame.display.update()

displayloadingscreen(WIN)