from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS

class Shot(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius)
    
    def update(self,dt):
        self.position += self.velocity * dt

