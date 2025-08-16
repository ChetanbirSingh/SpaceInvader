import pygame
from Entities.entity import Entity

class Player(Entity):
    def __init__(self, img_path, x, y, screen_width, screen_height, velocity=0, speed=1):
        super().__init__(img_path, x, y, screen_width, screen_height, speed)
        self.velocity = velocity

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.velocity = -self.speed
            elif event.key == pygame.K_RIGHT:
                self.velocity = self.speed

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.velocity = 0

    def update_position(self):
        self.x += self.velocity
        self.clamp_position()
