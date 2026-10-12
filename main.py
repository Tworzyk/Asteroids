import pygame
import sys
from constans import SCREEN_WIDTH,SCREEN_HEIGHT,PLAYER_RADIUS,HEALTH,NEXT_LIFE_SCORE
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
    
    next_life_score = NEXT_LIFE_SCORE

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x,y,PLAYER_RADIUS,HEALTH)
    
    
    while True:
        log_state()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player) and player.life.lifes <= 0:
                log_event("player_hit")
                print("Game over!")
                sys.exit(1)
            elif asteroid.collides_with(player):
                player.life.removelife()
                player.respawn()
            
                
            for shot in shots:
                if asteroid.collides_with(shot):
                    point.addpoints()
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    
                    if point.points >= next_life_score:
                        player.life.addlife()
                        next_life_score +=10

       
        for d in drawable:
            d.draw(screen)


    

        score_text = font.render(f"Points: {point.points}", True, "white")
        life_text = font.render(f"Lives: {player.life.lifes}",True,"white")
        life_rect = score_text.get_rect(topright=(SCREEN_WIDTH - 20, 40))
        text_rect = score_text.get_rect(topright=(SCREEN_WIDTH - 20, 20))
        screen.blit(score_text, text_rect)
        screen.blit(life_text,life_rect)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
