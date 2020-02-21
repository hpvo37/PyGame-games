import pygame, pygame.font, pygame.event, pygame.draw, string
from tkinter import *
from pygame.locals import *

import pygame
import random
import os


def get_key():
  while 1:
    event = pygame.event.poll()
    if event.type == KEYDOWN:
      return event.key
    else:
      pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + "".join(current_string))
  while 1:
    inkey = get_key()
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == K_RETURN:
      colors()  
      break
    elif inkey == K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + "".join(current_string))
  return "".join(current_string)



#---use range random to generate different colors-----
def colors():
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
    screen = pygame.display.set_mode((380,260))
    pygame.display.flip()
    while True:
        #your code here
        if playing:            
                screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        pygame.display.flip()
        root.update()
def main():
  screen = pygame.display.set_mode((320,240))
  print (ask(screen, "Guess Color") + " was incorrect")

if __name__ == '__main__': main()
