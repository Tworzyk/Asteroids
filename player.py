from circleshape import CircleShape
from constans import LINE_WIDTH

import pygame
class Player(CircleShape):
    
    rotation: int = 0
    
    def __init__(self, pos_x: float, pos_y: float,Player_Radius: float):
        super().__init__(pos_x,pos_y,Player_Radius)
        

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def draw(self,screen: pygame):
        pygame.draw.polygon(screen,"white",self.triangle(),LINE_WIDTH)