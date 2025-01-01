#this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *

def main():
    #initialize pygame
    pygame.init()
    #initialize the clock
    clock=pygame.time.Clock()
    dt=0

    print(f"pygame is initialized is {pygame.get_init()}")
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #initialize the screen
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    #initialize the player
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
    #initialize groups
    drawable=pygame.sprite.Group()
    updatable=pygame.sprite.Group()
    Player.containers(drawable,updatable)
    #game loop
    while True:
        pygame.Surface.fill(screen,(0,0,0))
        for updtbl in updatable:
            updtbl.update(dt)
        for drwbl in drawable:
            drwbl.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #tick the framerate    
        dt=clock.tick(60)/1000


if __name__== "__main__":
    main()