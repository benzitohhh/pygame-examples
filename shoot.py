import random, os.path

import sys
import pygame

SCREEN_SIZE = (600, 480)

RED = (255, 0, 0)
YELLOW = (255, 255, 0)

#main_dir = os.path.split(os.path.abspath(__file__))[0]
main_dir = './'

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert_alpha()

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs


class Zombie(pygame.sprite.Sprite):
    speed = 2
    images = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect = self.rect.move(self.speed, 0)    
        if self.rect.x > 500:
            self.rect.x = 0

            
class Weapon(pygame.sprite.Sprite):
    images = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = pygame.mouse.get_pos()

        
def main():
    # Initialize pygame
    pygame.init()

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    #Load images, assign to sprite classes
    #(do this before the classes are used, after screen setup)
    img = load_image('data/zombie.png')
    Zombie.images = [img, pygame.transform.flip(img, 1, 0)]
    img = load_image('data/grenade.png')
    Weapon.images = [img]
    
    # clock
    clock = pygame.time.Clock()
    
    # create the background
    background = pygame.Surface(SCREEN_SIZE)
    background.fill(RED)
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Initialize Game Groups
    zombies = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()

    # Assign default groups to each sprite class
    Zombie.containers = zombies, all
    Weapon.containers = all

    # initialize our starting sprites
    Zombie() # note, this 'lives' because it goes into a sprite group
    Weapon()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 pygame.quit()
                 return
                 #sys.exit()

        keystate = pygame.key.get_pressed()

        # clear/erase the last drawn sprites
        all.clear(screen, background)

        # update all the sprites
        all.update()

        # TODO: handle player input
        # TODO: detech collisions

        #draw the scene
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # cap the framerate
        clock.tick(40)
                
    pygame.quit()

    
#call the "main" function if running this script
if __name__ == '__main__': main()

#main()