import random
from Entities.entity import Entity

class Enemy(Entity):
    def __init__(self, img_path, screen_width, screen_height, speed=1):
        # Random initial position
        x = random.randint(0, screen_width)
        y = random.randint(50, 150)

        super().__init__(img_path, x, y, screen_width, screen_height, speed)

    def re_spawn(self):
        self.x = random.randint(0, self.screen_width - 64)
        self.y = random.randint(50, 150)

    def update_position(self):
        # Move horizontally
        self.x += self.speed

        # Bounce off left and right edge
        if self.x <= 0 or self.x >= self.screen_width - self.image.get_width():
            self.speed = -self.speed  # reverse horizontal direction by flipping the sign
            self.y += 40