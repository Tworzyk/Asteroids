from circleshape import CircleShape
from constans import SHOT_RADIUS
import pygame


class Shot(CircleShape):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x,y,SHOT_RADIUS)


    def update(self, dt: float) -> None:
        self.position += self.velocity *dt

    def draw(self,surface: pygame) -> None:
        pygame.draw.circle(
            surface,
            "white",
            self.position,
            self.radius,
            SHOT_RADIUS
            )