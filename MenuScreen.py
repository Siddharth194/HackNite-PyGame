import pygame
from basicfuncs import *
from config import *
from images import *
from LoadingScreen import *

pygame.init()

def displaymenuscreen(WIN):

    running=True

    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        WIN.fill((0,0,0))
        WIN.blit(loadingscreen,(0,0))
        #Donefont = pygame.font.Font('resources/fonts/RedHatText-Medium.ttf', 100)
        #Donefont1 = Donefont.render("DONE", True, (178,161,223))
        

        startfont = pygame.font.Font('resources/fonts/RedHatText-Medium.ttf',30)
        startfont1 = startfont.render("A Slippery Situation",True, (178,161,223))
        startfont2 = startfont.render("PLAY",True, (178,161,223))
        r=pygame.draw.rect(WIN,(0,0,0),[300,300,300,50])

        for event in pygame.event.get():


            if event.type==pygame.MOUSEBUTTONDOWN:
                if 300<=mouse[0]<=600 and 300<=mouse[1]<=350:
                    return

        #WIN.blit(Donefont1,(310,220))
        WIN.blit(startfont1, (325,150))
        WIN.blit(startfont2,(400,300))
        
        pygame.display.update()



