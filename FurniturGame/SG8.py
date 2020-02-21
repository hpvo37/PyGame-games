from pygame import *
import sys
import pygame
import time
import random

pygame.init()

display_width= 600
display_height= 500

black=(0,0,0)
white=(255,255,255)
light_grey=(190, 193, 198)
dark_grey=(77, 77, 77)

red = (200, 0,0)
green = (0,200,0)
blue = (0,0,200)

yellow1=(214, 214, 162)
yellow2=(237, 239, 167)

#-IMAGES-
background = pygame.image.load('background.png')
housewcursor = pygame.image.load('housewcursor.png')
chairselection1 =pygame.image.load('chairslection1.png')
chairselection2 =pygame.image.load('chairslection2.png')
chair1 =pygame.image.load('chair1.png')
chair2 =pygame.image.load('chair2.png')

#-INDOORS, ASSETS-
indoor = pygame.image.load('indoors.png')
#-----chair----
chairselect= pygame.image.load('chairselection.png')

#---START SET---
gameDisplay= pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('BEST OTOME EVER')
clock=pygame.time.Clock()

#-TEXT-
def text_objects(text, font):
    textSurface=font.render(text,True,dark_grey)
    return textSurface,textSurface.get_rect()

#-BUTTON-
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0]==1 and action !=None:
            action()             
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

        #TEXT ON BUTTON
    smallText=pygame.font.SysFont('Berlin Sans FB',20)
    textSurf, textRect=text_objects(msg,smallText)
    textRect.center=((x+(w/2)),(y+h/2))
    gameDisplay.blit(textSurf, textRect)

#-CURSOR DETECT-
def playicon(playicon_image,xi,xf,yi,yf,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if xf>mouse[0]>xi and yf>mouse[1]>yi:
        gameDisplay.blit(playicon_image, (xi,yi))
        if  click[0]==1 and action !=None:
            action()

#---Selection button-
def select(x,y,w,h,option,a,b,image):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if w>mouse[0]>x and h>mouse[1]>y:
        x=0;
        gameDisplay.blit(option,(x,y))
        if click[0]==1:
            gameDisplay.blit(image, (a,b))
            x = x + 1
        if x ==1:
            gameDisplay.blit(image, (a,b))

#--Chair select menu
def chairselection():
    chairselects=True
    while chairselects:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.blit(indoor, (0,0))
        gameDisplay.blit(chairselect, (299,20))
        button("BACK", 50,20, 100,45, light_grey, white, game_loop)
        button("CHAIR",450, 20,100,45, yellow1, yellow2, chairselection)
        button("TABLE",450, 76,100,45, yellow1, yellow2, game_loop)
        select(297,19,375,70,chairselection1, 140,160, chair1)
        select(375,20,454,70,chairselection2, 140,160, chair2)
        pygame.display.update()
        
        clock.tick(60)     
    

#-CHAIR-
def placefurniture(x,y,image):
      while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #place furniture
        gameDisplay.blit(image, (x,y))    
        pygame.display.update()
        
        clock.tick(60)  
       
#-INDOORS-
def indoors():
    indoors=True
    while indoor:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.blit(indoor, (0,0))
        button("BACK", 50,20, 100,45, light_grey, white, game_loop)
        button("CHAIR",450, 20,100,45, yellow1, yellow2, chairselection)
        button("TABLE",450, 76,100,45, yellow1, yellow2, game_loop)
        pygame.display.update()
        clock.tick(60)     

#---GAME DEF---
def game_loop():
    global pause
    gameExit=False
    while not gameExit:
        FPS= random.randrange(100, 900)
        seconds = clock.tick(FPS) / 1000.0  # 'seconds' is the amount of seconds each loop takes.
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(background, (0,0))
        playicon(housewcursor, 82,489,22,378,indoors )
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
    
