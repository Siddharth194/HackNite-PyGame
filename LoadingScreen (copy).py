import pygame
from basicfuncs import *
from config import *
from images import *
from MenuScreen import *

pygame.init()



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
                templist = faderepeat(opacity,LOADINGSCREENDONEFADEOUT,200,50,textfademultiplier)
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

            for proceedcheck in pygame.event.get():
                if proceedcheck.type == pygame.KEYDOWN:
                    running = False
                    break
            

        pygame.display.update()
