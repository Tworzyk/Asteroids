from circleshape import CircleShape
from constans import LINE_WIDTH,ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius:float) -> None:
        super().__init__(x, y, radius)
        
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH,
        )
    
    def update(self,dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        
        left =self.velocity.rotate(random.uniform(20,50))
        right = self.velocity.rotate(random.uniform(20,50) * -1)


        new_radius = self.radius - ASTEROID_MIN_RADIUS

        samllerasteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
        samllerasteroid2 = Asteroid(self.position.x,self.position.y,new_radius)

        samllerasteroid1.velocity = left * 1.2
        samllerasteroid2.velocity = right * 1.2
        