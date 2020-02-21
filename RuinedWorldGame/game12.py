import pygame
import time
import random

pygame.init()

#-------------------COLORS--------------------

#-Basics
black = (0,0,0)
white = (255,255,255)
#-Others
light_blue = (153,217,234)
dark_blue = (121,215,255)
purple_blue = (112,146,190)

light_grey =(191, 191, 191)

#---------------------------------------------IMAGES----------------------------------------------
#IMAGES BACKGROUND
backgroundm = pygame.image.load('menubackground.jpg')
icon=pygame.image.load('icon.png')
slide1=pygame.image.load('slide1.png')

#KYLEJOB IMAGE
kylejob=pygame.image.load('KyleNarration.png')
#KYLE OFFICE
sKyle =pygame.image.load('seriousKyle.png')

#SCREEN
background_size = backgroundm.get_size()
background_rect = backgroundm.get_rect()
display_width,display_height = background_size
#---START SET---
gameDisplay= pygame.display.set_mode(background_size)
option1=pygame.image.load("option1.png").convert()
#OFFICE IMAGES
theoffice = pygame.image.load("theOffice.png").convert()
storyBox = pygame.image.load("storyBox.png")
talkBox = pygame.image.load("talkBox.png")
#OPTIONS IMAGES
opt1 = pygame.image.load('higlightOpt1.png')
opt2 = pygame.image.load('higlightOpt2.png')
opt3 = pygame.image.load('higlightOpt3.png')

#------------------------------------------------------------------------------------------------

#------------------INTRO IMAGES----------------------
world = pygame.image.load("2179world.png").convert()
city = pygame.image.load("BlackAppleCity.png").convert()
cityonfire = pygame.image.load("BlackAppleCityonfire.png").convert()
runningCrowd =pygame.image.load("runningCrowd.png").convert()
organization=pygame.image.load("organization.png").convert()

pygame.display.set_caption('What do you choose?')
clock=pygame.time.Clock()

pygame.display.set_icon(icon)
pause = True
running = True

#------------------FUNCTIONS-----------------------




def text_objects(text, font):
    textSurface=font.render(text,True,purple_blue)
    return textSurface,textSurface.get_rect()

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
    smallText=pygame.font.SysFont(None,40)
    textSurf, textRect=text_objects(msg,smallText)
    textRect.center=((x+(w/2)),(y+h/2))
    gameDisplay.blit(textSurf, textRect)


def chosing(x,y,w,h,option,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if w>mouse[0]>x and h>mouse[1]>y:
        gameDisplay.blit(option,(x,y))
        if click[0]==1 and action !=None:
            action()

    
    
def display_text_animation(string,x,y,speed,color):
    text = ''
    for i in range(len(string)):
        text += string[i]
        font=pygame.font.SysFont('Berlin Sans FB',40)
        text_surface = font.render(text, True, color)      

        text_rect = text_surface.get_rect()
        text_rect= (x,y)
        gameDisplay.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(speed)
    gameDisplay.blit(text_surface, text_rect)


def text(string,x,y):
    text=string
    font=pygame.font.SysFont('Berlin Sans FB',40)
    text_surface = font.render(text, True, black)      

    text_rect = text_surface.get_rect()
    text_rect= (x,y)
    gameDisplay.blit(text_surface, text_rect)
    pygame.display.update()

       
def quitgame():
    pygame.quit()
    quit()

def paused():

    #pygame.mixer.music.pause()    
    largeText=pygame.font.SysFont('Berlin Sans FB',80)
    TextSurf,TextRect=text_objects("PAUSED",largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            

        #---BUTTON--
        button("Continue",150,500,200,100,light_blue,dark_blue,unpause)
        button("Quit",900,500,200,100,light_blue,dark_blue,quitgame) 

        
        pygame.display.update()
        clock.tick(60)
        

    
#-----------------SLIDE SCENERIO--------------------
def slide(slidepicture,string1,string2,x,y1,y2):
    global pause
    gameDisplay.blit(slidepicture,background_rect)
    display_text_animation(string1,x,y1,black)
    display_text_animation(string2,x,y2,black)

    gameExit=False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        text(string1,x,y1)
        text(string2,x,y2)     

       
        clock.tick(200)
def fadein(fade,x,y):
    for i in range(255):
        if i==254:
            break 
        gameDisplay.fill((0,0,0))
        fade.set_alpha(i)
        gameDisplay.blit(fade, (x,y))
        pygame.display.flip()
        clock.tick(70)

#--------------------INTRO MENU--------------------
def game_intro():
    #-INTRO MUSSIC-
    #---pygame.mixer.music.load('intro.ogg')
    #---pygame.mixer.music.play(-1)
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()     
       


        #-INTRO DISPLAY-
        gameDisplay.blit(backgroundm,(0,0))
        #---gameDisplay.blit(header,(300,75))

        #---BUTTON--
        button("Play",470,100, 250,50,light_grey,white,introduction)
       # button("QUIT",650,500,300,100,light_blue,dark_blue,quitgame) 

        
        pygame.display.update()
        clock.tick(60)

#-------------------GAME INTRODUCTION-------------------
def introduction():
    fadein(world,0,0)
    gameDisplay.blit(world, (0,0))
    display_text_animation('Year 2179...',500,100,50,black)

    gameExit=False   
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()  
        click1 = pygame.mouse.get_pressed()
        if click1[0] !=1:            
            gameDisplay.blit(world, (0,0))
            text('Year 2179...',500,100)
            pygame.display.update()
            clock.tick(200)
        else:
            break
    introduction2()
        
def introduction2():
    fadein(city,0,0)
    display_text_animation('At Black Apple city,',500,500,30,black)
    display_text_animation('Cyber Crimes are increasing rapidly.',500,600,20,black)
    pygame.display.update()


    gameExit1=False   
    while not gameExit1:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()  
        click = pygame.mouse.get_pressed()
        if click[0] ==1:
            break
    game_loop()
    
#-----------------------MAIN GAME------------------------------
def game_loop():
    global pause
    gameDisplay.blit(slide1,background_rect)
    display_text_animation('Hi, my name is Kyle',620,436,50,black)
    display_text_animation('I am...',620,466,50,black)

    gameExit=False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        click = pygame.mouse.get_pressed()
        if click[0] !=1:
            text('Hi, my name is Kyle',620,436)
            text('I am...',620,466)
        else:
            break
    fadein(option1,0,0)
    kyleOptions()
def kyleOptions():
    gameExit = False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()  
               
        gameDisplay.blit(option1, (0,0))
        
        chosing(22,123,321,539,opt1,actor)
        chosing(420,125,735,550,opt2,gymnastic)
        chosing(840,127,1168,554,opt3,businessman)
        pygame.display.update()
        clock.tick(200)

#----------------------------KyleJOB-------------------------------------------
def businessman():
    gameDisplay.blit(kylejob, (0,0))
    display_text_animation('Kyle - your partner - is a businessman', 300,250,10,black)
    display_text_animation('He has a lot of connections...and money $',300,300,10,black)
    pygame.display.update()
    gameExit=False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        click = pygame.mouse.get_pressed()
        if click[0] ==1:
            break
    office()
def actor():
    gameDisplay.blit(kylejob, (0,0))
    display_text_animation('Kyle - your partner - is an actor', 300,250,10,black)
    display_text_animation('He can disguise as anyone and fit in easily',300,300,10,black)
    pygame.display.update()
    gameExit=False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        click = pygame.mouse.get_pressed()
        if click[0] ==1:
            break
    office()
def gymnastic():
    gameDisplay.blit(kylejob, (0,0))
    display_text_animation('Kyle - your partner - is a gymnastic', 300,250,10, black)
    display_text_animation('He can get through any security threat',300,300,10, black)
    pygame.display.update()
    gameExit=False
    
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                
        click = pygame.mouse.get_pressed()
        if click[0] ==1:
            break
    office()
#-----------------------OFFICE SCENE 1: OFFICE APPEARS-------------------------
def office():
    
    gameDisplay.blit(theoffice, (0,0))
    gameDisplay.blit(storyBox, (250,200))
    display_text_animation('You two are standing in Kyle s office',310,270,20,black)   
    display_text_animation('Kyle s looking at you,',310, 330,20,black)
    pygame.time.wait(1300)
    display_text_animation(' waiting...',600,330,20,black)

    pygame.display.flip()   

    gameExit = False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        click = pygame.mouse.get_pressed()
        if click[0] ==1:
            break
    kyleOffice()
    
#------------------------KYLE APPEARS IN THE OFFICE-----------------------------
def kyleOffice():
    gameDisplay.blit(theoffice, (0,0))
    gameDisplay.blit(talkBox, (300,200))
    gameDisplay.blit(sKyle, (42,70))
    text('Kyle',380,240)
    display_text_animation('So, what do you think?',360,350,40,black)   
    pygame.display.update() 
    gameExit = False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        click = pygame.mouse.get_pressed()
        if click[0] ==1:
            break
    blackscreen(theoffice,0,0,afterBlack)
    
#THIS IS WHAT HAPPEN-
def afterBlack():
    gameDisplay.fill((0,0,0))
    gameDisplay.blit(storyBox, (260,250))
    text('Kyle',380,240)
    display_text_animation('This is what happened...',360,320,40,black)   
    pygame.display.update() 
    gameExit = False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        click = pygame.mouse.get_pressed()
        if click[0] ==1:
            break
    BlitandClick(cityonfire,"Year 2100...")
    organizationExplained()
 

#-------------------------ORGANIZATION EXPLAINED---------------------------
def BlitandClick(blitImage,sentence):
    gameDisplay.blit(blitImage,(0,0))
    display_text_animation(sentence,550,550,70,white)
    pygame.display.update()
    clock.tick(50)
    gameExit = False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        click = pygame.mouse.get_pressed()
        if click[0] ==1:
            break
        '''for i in range(255):
        if i==254:
            break 
        gameDisplay.fill(black)
        storyBox.set_alpha(i)
        gameDisplay.blit(storyBox, (260,250))
        pygame.display.flip()
        clock.tick(70)
    gameDisplay.blit(organization,(0,0))
    gameDisplay.blit(storyBox, (260,250))
 
    display_text_animation('This is what happen...',360,320,40,black)
    pygame.display.update()
    gameExit = False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        click = pygame.mouse.get_pressed()
        if click[0] ==1:
            break'''
\
 



 
    
#------------------------ORGANIZATION EXPLAINED--------------------------------
def organizationExplained():
    fadein(organization,0,0)
    gameDisplay.blit(organization,(0,0))
    gameDisplay.blit(storyBox, (260,400))
    display_text_animation('An organization was formed...',330,470,40,black)
    display_text_animation('They took control and formed a new world.',330,510,40,black)
    
    gameExit = False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        click = pygame.mouse.get_pressed()
        if click[0] ==1:
            break
    plainblackscreen(organization,0,0)
    introduction()
    pygame.display.update()
    clock.tick(50)
    
#------------------------BLACK SCREEN--------------------------------------------
def plainblackscreen(fade,x,y):
    for i in range(255):
        gameDisplay.fill((0,0,0))
        fade.set_alpha(255-i)
        gameDisplay.blit(fade, (x,y))
        pygame.display.flip()
        clock.tick(70)   
def blackscreen(fade,x,y,action = None):
    for i in range(255):
        gameDisplay.fill((0,0,0))
        fade.set_alpha(255-i)
        gameDisplay.blit(fade, (x,y))
        pygame.display.flip()
        clock.tick(70)
    action()
    
    
game_intro()       
pygame.quit()
quit()
