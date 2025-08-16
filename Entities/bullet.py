from Entities.entity import Entity

class Bullet(Entity):
    def __init__(self, x, y, screen_width, screen_height, speed=-3):
        super().__init__('Assets/Img/bullet.png', x, y, screen_width, screen_height, speed)

    def update_position(self):
        # Move vertically
        self.y += self.speed

