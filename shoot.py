from circleshape import CircleShape
from constans import SHOT_RADIUS
import pygame


class Shot(CircleShape):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x,y,SHOT_RADIUS)


    def update():

    def draw(surface: pygame) -> None:
        pygame.draw.polygon(surface,)