import pygame
import time
import random

pygame.init()

#COLORS

#-Basics
black = (0,0,0)
white = (255,255,255)
#-Others
light_blue = (153,217,234)
dark_blue = (121,215,255)
purple_blue = (112,146,190)
#IMAGES
emma=pygame.image.load('Emma.png')
outfit1=pygame.image.load('outfit1.png')
outfit2=pygame.image.load('outfit2.png')
out1=pygame.image.load('out1.png')
out2=pygame.image.load('out2.png')

#SCREEN
background_size = emma.get_size()
background_rect = emma.get_rect()
display_width,display_height = background_size
#---START SET---
gameDisplay= pygame.display.set_mode(background_size)

pygame.display.set_caption('Fashion Stickman')
clock=pygame.time.Clock()
#FUNCTIONS
def button(x,y,w,h,a,b,c,d,option1,option2):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        gameDisplay.blit(option1,(x,y))
    if a+c>mouse[0]>a and b+d>mouse[1]>b:
        gameDisplay.blit(option2,(a,b))
    
def game_loop():
    gameExit=False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.blit(emma,(0,0))
        button(360,48,470,200,480,50,590,200,out1,out2)
        
        pygame.display.update()
        clock.tick(60)
        
game_loop()
pygame.quit()
quit()
