from circleshape import CircleShape
from logger import log_event
from constants import LINE_WIDTH
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rand = random.uniform(20,50)
        first = self.velocity.rotate(rand)
        second = self.velocity.rotate(-rand)
        new = self.radius - ASTEROID_MIN_RADIUS
        first_aste = Asteroid(self.position.x, self.position.y, new)
        second_aste = Asteroid(self.position.x, self.position.y, new)
        first_aste.velocity = first * 1.2
        second_aste.velocity = second * 1.2 
        
