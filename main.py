import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    numpass, numfail = pygame.init()
    #print(f"P:{numpass}, F:{numfail}")

    #get a new GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    field = AsteroidField()
    
    Shot.containers = (shots, updatable, drawable)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.colliding(player):
                #TODO: Update screen w/ "GAME OVER" text and skip re-draw loop
                print("Game Over")
                sys.exit(1)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.colliding(shot):
                    shot.kill()
                    asteroid.split()
        
        screen.fill("black")
        
        for drawn in drawable:
            drawn.draw(screen)
                
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick() / 1000

if __name__ == "__main__":
    main()
