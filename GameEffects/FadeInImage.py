import pygame
pygame.display.init()
screen = pygame.display.set_mode((800,600))
logo = pygame.image.load("menubackground.png").convert()
clock = pygame.time.Clock()

# fade in the logo
for i in range(255):
    screen.fill((0,0,0))
    logo.set_alpha(i)
    screen.blit(logo, (0,0))
    pygame.display.flip()
    clock.tick(10)
    
pygame.quit()
quit()
