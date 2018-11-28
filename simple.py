import sys
import pygame

RED = (255, 0, 0)
YELLOW = (255, 255, 0)

zombie_img = pygame.image.load("zombie.png")
grenade_img = pygame.image.load("grenade.png")

pygame.init()
screen = pygame.display.set_mode((600, 480))

# Gives a rectangle bounding box (has x, y, width, height)
zombie_rect = zombie_img.get_rect() # defaults to 0, 0
zombie_rect.x = 0

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             done = True
             continue
             #sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('woooop')

    # Background
    screen.fill(RED)

    # Render Zombie
    a = screen.blit(zombie_img, (100, 100, 20, 20))

    pygame.display.update()
