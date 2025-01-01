#this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
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

    #initialize groups
    asteroids=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    updatable=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    Player.containers=(drawable,updatable)
    Asteroid.containers=(asteroids,drawable,updatable)
    AsteroidField.containers=(updatable)
    Shot.containers=(shots)
    #initialize the player
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
    ast_field=AsteroidField()
    #game loop
    while True:
        pygame.Surface.fill(screen,(0,0,0))
        for updtbl in updatable:
            updtbl.update(dt)
        for drwbl in drawable:
            drwbl.draw(screen)
        for shts in shots:
            shts.draw(screen)
            shts.update(dt)
        pygame.display.flip()
        for astrd in asteroids:
            if astrd.collision(player) == True:
                print("Game over!")
                exit()
        for astrd in asteroids:
            for sht in shots:
                if astrd.collision(sht) == True:
                    sht.kill()
                    astrd.split()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #tick the framerate    
        dt=clock.tick(60)/1000


if __name__== "__main__":
    main()