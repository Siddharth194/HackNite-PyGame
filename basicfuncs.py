import pygame
pygame.init()

def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))

        temp.convert()

        temp.set_alpha(opacity)

        target.blit(temp, location)


def faderepeat(opacity,speed,ulimit,dlimit,mult):

        if opacity <= dlimit:
                mult = 1

        elif opacity >= ulimit:
                mult = -1

        opacity += mult*speed
        return (opacity,mult)


def im(dest):
    return pygame.image.load(dest)
