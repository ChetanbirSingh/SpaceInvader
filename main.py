import pygame
import math

from Entities.player import Player
from Entities.enemy import Enemy

pygame.init()

screen_width = 1000
screen_height = 700

player_score = 0

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('Assets/Img/logo.png')
pygame.display.set_icon(icon)

background = pygame.image.load('Assets/Img/background.jpg')

# Create player instance
player = Player(img_path='Assets/Img/player.png', x=370, y=580, screen_width=screen_width, screen_height=screen_height)

# Create enemy instance
enemy = Enemy(img_path='Assets/Img/Enemies/enemy.png', screen_width=screen_width, screen_height=screen_height)


def is_collision(player, enemy):
    distance = math.sqrt(math.pow((bullet.x - enemy.x), 2) + math.pow(bullet.y - enemy.y, 2))
    return distance < 27

running = True
while running:
    # Process all events (keyboard, mouse, window close, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the game loop when the window is closed
        player.handle_input(event)  # Update player velocity based on key events

    # Update game state
    player.update_position()  # Move the player according to current velocity

    screen.fill((25, 23, 25))
    # Background Image
    screen.blit(background, (0, 0))
    player.display(screen)     # Draw the player on the screen

    # Bullets
    player.update_position()
    player.update_bullets()
    player.display(screen)
    player.display_bullets(screen)

    # Collision
    for bullet in player.bullets[:]:  # iterate over a copy to safely remove
        bullet.update_position()
        if is_collision(bullet, enemy):
            player.bullets.remove(bullet)
            player_score += 1
            print(player_score)
            enemy.re_spawn()

    enemy.display(screen)      # Draw the enemy on the screen
    enemy.update_position()    # Move the enemy

    pygame.display.update()    # Refresh the display with the new frame
