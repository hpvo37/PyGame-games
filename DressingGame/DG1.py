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
mscreen = pygame.image.load('mainscreen.png')
normalclothes = pygame.image.load('normalclothes.png')
back = pygame.image.load('back.png')

emma=pygame.image.load('Emma.png')
outfit1=pygame.image.load('outfit1.png')
outfit2=pygame.image.load('outfit2.png')
outfit3=pygame.image.load('outfit3.png')
outfit4=pygame.image.load('outfit4.png')
outfit5=pygame.image.load('outfit5.png')
outfit6=pygame.image.load('outfit6.png')
outfit7=pygame.image.load('outfit7.png')
out7=pygame.image.load('out7.png')
out6=pygame.image.load('out6.png')
out4=pygame.image.load('out4.png')
out3=pygame.image.load('out3.png')
out1=pygame.image.load('out1.png')
out2=pygame.image.load('out2.png')
out5=pygame.image.load('out5.png')

#SCREEN
background_size = emma.get_size()
background_rect = emma.get_rect()
display_width,display_height = background_size
#---START SET---
gameDisplay= pygame.display.set_mode(background_size)

pygame.display.set_caption('Fashion Stickman')
clock=pygame.time.Clock()
#FUNCTIONS
def button(x,y,w,h,option,wear,a,b,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if w>mouse[0]>x and h>mouse[1]>y:
        gameDisplay.blit(option,(x,y))
        if click[0]==1 and action !=None:
            action(wear,a,b)

def nbutton(x,y,w,h,option,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if w>mouse[0]>x and h>mouse[1]>y:
        gameDisplay.blit(option,(x,y))
        if click[0]==1 and action !=None:
            action()

def main_screen():
    gameExit=False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(mscreen,(0,0))
        nbutton(264,255,637,547,normalclothes,game_loop)
        pygame.display.update()
        clock.tick(60)
        
def wearing(outfit,a,b):
    gameExit=False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.blit(emma,(0,0))
        gameDisplay.blit(outfit,(a,b))
        nbutton(816,7,851,46,back,main_screen)
        button(360,48,480,244,out1,outfit1,11,230,wearing)
        button(482,50,598,244,out2,outfit2,37,197,wearing)
        button(601,55,722,240,out3,outfit3,37,265,wearing)
        button(725,54,848,249,out4,outfit4,2,267,wearing)
        button(357,249,480,445,out5,outfit5,2,260,wearing)
        button(487,252,609,499,out6,outfit6,25,258,wearing)
        button(615,253,730,445,out7,outfit7,90,250,wearing)
        pygame.display.update()
        clock.tick(60)

def game_loop():
    gameExit=False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.blit(emma,(0,0))
        nbutton(816,7,851,46,back,main_screen)
        button(360,48,480,244,out1,outfit1,11,230,wearing)
        button(482,50,598,244,out2,outfit2,37,197,wearing)
        button(601,55,722,240,out3,outfit3,37,265,wearing)
        button(725,54,848,249,out4,outfit4,2,267,wearing)
        button(357,249,480,445,out5,outfit5,2,260,wearing)
        button(487,252,609,499,out6,outfit6,25,258,wearing)
        button(615,253,730,445,out7,outfit7,90,250,wearing)
        pygame.display.update()
        clock.tick(60)
        
main_screen()
pygame.quit()
quit()
