import pygame
import sys
import pygame.sprite as sprite

theClock = pygame.time.Clock()

background = pygame.image.load('background.png')

background_size = background.get_size()
background_rect = background.get_rect()
screen = pygame.display.set_mode(background_size)
w,h = background_size
x = 0
y = 0

x1 = 0
y1 = -h

running = True

while running:
    screen.blit(background,background_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    y1 += 6
    y += 6
    screen.blit(background,(x,y))
    screen.blit(background,(x1,y1))
    if y > h:
        y = -h
    if y1 > h:
        y1 = -h
    theClock.tick(10)
    pygame.display.flip()
    pygame.display.update()
    
pygame.quit()
quit()
