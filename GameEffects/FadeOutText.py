import pygame
from pygame.locals import *

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
backgroundm = pygame.image.load('menubackground.png')

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

def fadeintext(string,a,b):
    textToFadeOut = string
    myFont=pygame.font.SysFont('Berlin Sans FB',40)
    label = myFont.render(textToFadeOut,1,(0,0,0))    
    newSurf = pygame.Surface(myFont.size(textToFadeOut))
    newSurf.fill(WHITE)
    newSurf.blit(label,(a,b))
    
    for x in range(220):
        screen.fill(WHITE)#or whatever your background color is
        newSurf.set_alpha(x)
        screen.blit(newSurf, (a,b))
        pygame.display.flip()
        pygame.time.delay(8)
        a+=0.1
        b+=0.1
    for x in range(220):
        screen.fill(WHITE)  #or whatever your background color is
        newSurf.set_alpha(225-x)
        screen.blit(newSurf, (a,b))
        pygame.display.flip()
        pygame.time.delay(8)

fadeintext('+Smooth Talk',0,0)
pygame.quit()
quit()
