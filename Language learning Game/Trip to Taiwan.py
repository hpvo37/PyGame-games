from pygame import *
import sys
import pygame
import time
import random

pygame.init()

#---WIDTH,HEIGHT,COLORS,MEASUREMENTS SET---
display_width=600
display_height=400

black=(0,0,0)
white=(255,255,255)
light_grey=(164, 166, 171)
dark_grey=(77, 77, 77)

light_blue =(102, 204, 255)

red=(200,0,0)
green=(0,200,0)
blue=(0,0,200)

bright_green=(102, 255, 102)
bright_red=(255, 77, 77)


#-IMAGES-
background=pygame.image.load('Taiwan.JPG')
mainim=pygame.image.load('firstmain.PNG')
repl = pygame.image.load('firstreply.PNG')
maini = pygame.image.load('main.png')
op_1 = pygame.image.load('op_1.png')

#--ICONS--
message = pygame.image.load('messageicon.png')
firstmes = pygame.image.load('firstmessage.png')
mess2 = pygame.image.load('secondmessage.png')
messicon = pygame.image.load('messicon.png')
#---OPTIONS----
op1 = pygame.image.load('op1.png')
luggae = pygame.image.load('luggae.png')

#---START SET---

gameDisplay= pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A trip to Taiwan')
clock=pygame.time.Clock()

pause=True

#----DEF FUNCTIONS---
def mouse(x,y,w,h,args,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if w>mouse[0]>x and h>mouse[1]>y:
        if click[0]==1 and action !=None:
            action(*args)
            
def text(string,x,y):
    text=string
    font=pygame.font.SysFont('Berlin Sans FB',30)
    text_surface = font.render(text, True, black)      

    text_rect = text_surface.get_rect()
    text_rect= (x,y)
    gameDisplay.blit(text_surface, text_rect)
    pygame.display.update()

def display_text_animation(string,x,y,speed,color):
    text = ''
    for i in range(len(string)):
        text += string[i]
        font=pygame.font.SysFont("monospace", 18)
        text_surface = font.render(text, True, color)      

        text_rect = text_surface.get_rect()
        text_rect= (x,y)
        gameDisplay.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(speed)
    gameDisplay.blit(text_surface, text_rect)
    
def text_objects(text, font):
    textSurface=font.render(text,True,dark_grey)
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
    smallText=pygame.font.SysFont('Berlin Sans FB',20)
    textSurf, textRect=text_objects(msg,smallText)
    textRect.center=((x+(w/2)),(y+h/2))
    gameDisplay.blit(textSurf, textRect)
    
def paused():
    
    largeText=pygame.font.SysFont('Berlin Sans FB',110)
    TextSurf,TextRect=text_objects("PAUSED",largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            

        #---BUTTON--
        button("CONTINUE",150,450,100,50,light_grey,white,unpause)
        button("QUIT",550,450,100,50,light_grey,white,quitgame) 

        
        pygame.display.update()
        clock.tick(60)

def playicon(image,xi,xf,yi,yf,action =None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if xf>mouse[0]>xi and yf>mouse[1]>yi:
        gameDisplay.blit(image, (xi,yi))
        if click[0]==1 and action !=None:
            action()

#---FADE IN---
def fade_in(fadein_pic):
    
    #----FADE CREEN---
    alphaSurface = Surface((600,400)) # The custom-surface of the size of the screen.
    alphaSurface.blit(fadein_pic,(0,0)) # Fill it with whole white before the main-loop.
    alphaSurface.set_alpha(0) # Set alpha to 0 before the main-loop. 
    alph = 0 # The increment-variable.

    for x in range(0, 1000):
        gameDisplay.fill((0,0,0)) # At each main-loop fill the whole screen with black.
        alph += 0.2 # Increment alpha by a really small value (To make it slower, try 0.01)
        alphaSurface.set_alpha(alph) # Set the incremented alpha-value to the custom surface.
        gameDisplay.blit(alphaSurface,(0,0)) # Blit it to the screen-surface (Make them separate)

     # Flip the whole screen at each frame.
        display.flip()

#---INTRO MENU---
def game_intro():
    #-INTRO MUSSIC-
    pygame.mixer.music.load('intro.ogg')
    pygame.mixer.music.play(-1)
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()     
       

        #---INTRO DISPLAY----
        gameDisplay.blit(background, (0,0))


        #---BUTTON--
        button("PLAY",240,60,100,40,light_blue,white,option_1)
        #button("RESET",87,450,150,70,light_grey,white,quitgame) 
        #button("SETTINGS",324,450,150,70,light_grey,white) 
        #button("HELP",561,450,150,70,light_grey,white) 

        
        pygame.display.update()
        clock.tick(60)

def game_loop_1():
    fade_in(mainim)
    gameExit=False
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.blit(mainim, (0,0))
        button("MAIN MENU",475,20,100,30,white,light_grey,game_intro)
        playicon(message, 79,170,114,198, first_message)
        pygame.display.update()
        clock.tick(60)

#--FIRST MESSAGE----
def first_message():
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(180, 320, 800, 35)
    color_inactive = pygame.Color('black')
    color_active = pygame.Color('white')
    color = color_inactive
    active = False
    text = ''
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        reply (text)
                        print(text)
                        text = ''
                        
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        
        gameDisplay.blit(firstmes, (0,0))
        button("MAIN MENU",475,20,100,30,white,light_grey,game_intro)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        gameDisplay.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(gameDisplay, color, input_box, 2)

        pygame.display.update()
        clock.tick(60)

#---FIRST REPLY----
def reply(message):
    gameExit=False
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.blit(repl, (0,0))
        button("MAIN MENU",475,20,100,30,white,light_grey,game_intro)
        font = pygame.font.Font(None, 26)
        rep = font.render( message, True, black)
        gameDisplay.blit(rep, (475, 267))
        
        pygame.display.update()
        clock.tick(30)
        pygame.time.wait(1300)
        secondmess()

def secondmess():
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(mess2, (0,0))
        button("MAIN MENU",475,20,100,30,white,light_grey,game_intro)
        button("BACK",30,20,100,30,white,light_grey,game_loop_2)
        pygame.display.update()
        clock.tick(30)
        
def game_loop_2():
    gameExit=False
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        gameDisplay.blit(maini, (0,0))
        button("MAIN MENU",475,20,100,30,white,light_grey,game_intro)
        playicon(messicon, 79,170,114,198, first_message)
        pygame.display.update()
        clock.tick(60)
        pygame.time.wait(1300)
        option_1()

def option_1():
    global pause
    gameDisplay.blit(op_1,(0,0))
    display_text_animation('What will you pack for your flight?',50,300,30,white)
    
    gameExit=False
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        mouse( 507,367,550, 385,(op1,luggae,luggae,game_loop_2,game_loop_2),choice)
        pygame.display.update()
        clock.tick(60)
def choice(image,op1,op2,c1,c2):
    gameDisplay.blit(image,(0,0))
    gameExit=False
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        playicon(op1, 0,300,0,400,c1)
        playicon(op2, 300, 600,0,400,c2)
        pygame.display.update()
        clock.tick(60)
        
    
    
    

game_intro()
game_loop()
pygame.quit()
quit()
