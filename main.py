import pygame
import sys
from constans import SCREEN_WIDTH,SCREEN_HEIGHT,PLAYER_RADIUS
from logger import log_state,log_event
from player import Player
from Asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shot
from points import Points
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen HEIGHT: {SCREEN_HEIGHT}")
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots,drawable,updatable)
    

    point = Points()
    font = pygame.font.Font(None,36)

    asteroidfield = AsteroidField()

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x,y,PLAYER_RADIUS)
    
    
    while True:
        log_state()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit(1)
                
            for shot in shots:
                if asteroid.collides_with(shot):
                    point.addpoints()
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        
        for d in drawable:
            d.draw(screen)


    

        score_text = font.render(f"Points: {point.points}", True, "white")
        text_rect = score_text.get_rect(topright=(SCREEN_WIDTH - 20, 20))
        screen.blit(score_text, text_rect)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
