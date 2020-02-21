import pygame
from pygame.locals import *

from tkinter import *
from pygame.locals import *

import pygame
import random
import os
global playing

playing=False
def playpause():
    global playing
    if playing==True:
        playing=False
    else:
        playing=True
root = Tk()
embed = Frame(root, width=380, height=260)
embed.grid(row=0,column=2)
playpausebutton=Button(root, command=playpause, text="Play / Pause")
playpausebutton.grid(row=1,column=2)
root.update()

#---- use tinker interface----
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
pygame.display.init()
pygame.display.flip()
    


def name():
    pygame.init()
    screen = pygame.display.set_mode((480, 360))
    name = ""
    font = pygame.font.Font(None, 50)
    while playing:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    name = ""
                    if playing:            
                        screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
                    pygame.display.flip()
                    root.update()
                elif evt.key == K_SPACE:
                    name += " "
            elif evt.type == QUIT:
                return
        screen.fill((0, 0, 0))
        block = font.render(name, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()

if __name__ == "__main__":
    name()
    pygame.quit()
