from circleshape import CircleShape
from constans import LINE_WIDTH,PLAYER_TURN_SPEED,PLAYER_SPEED
from shoot import Shot
import pygame
class Player(CircleShape):
    
    
    
    def __init__(self, pos_x: float, pos_y: float,Player_Radius: float) -> None:
        super().__init__(pos_x,pos_y,Player_Radius)
        self.rotation: float = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def draw(self,screen: pygame) -> None:
        pygame.draw.polygon(screen,"white",self.triangle(),LINE_WIDTH)
        
    def rotate(self,dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
    def move(self,dt: float) -> None:
        unit_vector = pygame.Vector2(0,1)
        rotated_vetor = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vetor * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        shot = Shot(self.position)
        self.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_TURN_SPEED