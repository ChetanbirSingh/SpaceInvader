import pygame

class Entity:
    def __init__(self, img_path, x, y, screen_width, screen_height, speed=0.2):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(img_path)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def clamp_position(self):
        if self.x <= 0:
            self.x = 0
        elif self.x > self.screen_width - self.image.get_width():
            self.x = self.screen_width - self.image.get_width()
