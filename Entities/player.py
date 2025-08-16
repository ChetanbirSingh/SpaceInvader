import pygame

class Player:
    def __init__(self, img_path, x, y, screen_width, screen_height, velocity=0, speed=0.2):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.speed = speed
        self.image = pygame.image.load(img_path)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def display(self, screen):
        # Draw the player at its current position
        screen.blit(self.image, (self.x, self.y))

    def handle_input(self, event):
        # Handle key press events to set horizontal velocity
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.velocity -= self.speed  # move left
            elif event.key == pygame.K_RIGHT:
                self.velocity += self.speed   # move right

        # Handle key release events to stop movement
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.velocity = 0

    def update_position(self):
        # Update the player’s position based on current velocity
        self.x += self.velocity

        # Prevent the player from moving off the left edge
        if self.x <= 0:
            self.x = 0
        # Prevent the player from moving off the right edge
        elif self.x > self.screen_width - self.image.get_width():
            self.x = self.screen_width - self.image.get_width()
