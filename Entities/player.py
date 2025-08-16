import pygame
from pygame import mixer
from Entities.bullet import Bullet
from Entities.entity import Entity

class Player(Entity):
    def __init__(self, img_path, x, y, screen_width, screen_height, velocity=0, speed=5):
        super().__init__(img_path, x, y, screen_width, screen_height, speed)
        self.velocity = velocity
        self.bullets = []

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.velocity = -self.speed
            elif event.key == pygame.K_RIGHT:
                self.velocity = self.speed
            # Bullets
            elif event.key == pygame.K_SPACE:
                self.shoot()

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.velocity = 0

    def shoot(self):
        # Shoot a bullet from the center-top of the player
        bullet_x = self.x + self.image.get_width() // 2
        bullet_y = self.y
        self.bullets.append(Bullet(bullet_x, bullet_y, self.screen_width, self.screen_height))
        # Play sound
        mixer_sound = mixer.Sound('Assets/Audio/laser.wav')
        mixer_sound.play()

    def update_position(self):
        self.x += self.velocity
        self.clamp_position()

    def update_bullets(self):
        for bullet in self.bullets[:]:
            bullet.update_position()
            if bullet.y < 0:  # remove off-screen bullets
                self.bullets.remove(bullet)

    def display_bullets(self, screen):
        for bullet in self.bullets:
            bullet.display(screen)