from pygame import *
import pygame

black=(0,0,0)

screen = display.set_mode((1024,768))
alphaSurface = Surface((1024,768)) # The custom-surface of the size of the screen.
alphaSurface.fill((255,255,255)) # Fill it with whole white before the main-loop.
alphaSurface.set_alpha(0) # Set alpha to 0 before the main-loop. 
alph = 0 # The increment-variable.
for x in range(0, 500):
    screen.fill((0,0,0)) # At each main-loop fill the whole screen with black.
    alph += 0.6 # Increment alpha by a really small value (To make it slower, try 0.01)
    alphaSurface.set_alpha(alph) # Set the incremented alpha-value to the custom surface.
    screen.blit(alphaSurface,(0,0)) # Blit it to the screen-surface (Make them separate)

     # Flip the whole screen at each frame.
    display.flip()
    
    # Trivial pygame stuff.
    
for y in range(0, 500):
    screen.fill((255,255,255))
    pygame.draw.rect(screen, black,[2,2,20,200])
    display.flip()

    
pygame.quit()
quit()

     

