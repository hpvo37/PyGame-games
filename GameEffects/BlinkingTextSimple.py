import pygame

# initialize pygame, this must be called before
# doing anything with pygame
pygame.init()

# create a screen
screen = pygame.display.set_mode((400, 400))

# setup the text
font = pygame.font.Font(None, 36)
text = font.render("fcking hate quiz", True, (100, 100, 100))

display = True
run= True
# the main loop
while run:
     for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if 800>pos[0]>0 and 600>pos[1]>0:
                 run = False
          # empty the screen
     screen.fill((255, 255, 255))

     display = not display

     # draw the text to the screen only if display is True
     if display:
         screen.blit(text, (100, 100))

     # update the actual screen
     pygame.display.flip()

     # wait for half second
     pygame.time.wait(400)
pygame.quit()
quit()
