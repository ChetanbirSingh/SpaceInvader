import pygame
from pygame import mixer
import math
import random
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

# Background music
mixer.music.load('Assets/Audio/background.wav')
# Play music on loop
mixer.music.play(-1)

player = Player('Assets/Img/player.png', 370, 580, screen_width, screen_height)

enemies = []
spawn_timer = 0
spawn_interval = 120
MAX_ENEMIES = 8
max_speed = 2.5

font = pygame.font.Font('freesansbold.ttf', 32)

text_x = 10
text_y = 10

def display_score(x, y):
    score = font.render("Score: " + str(player_score), True, (255, 255, 255))
    screen.blit(score, (x, y))

def is_collision(sprite1, sprite2):
    distance = math.sqrt((sprite1.x - sprite2.x) ** 2 + (sprite1.y - sprite2.y) ** 2)
    return distance < 27

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.handle_input(event)

    player.update_position()
    player.update_bullets()

    # Make spawning random and harder with score
    spawn_timer += 1
    if spawn_timer >= spawn_interval and len(enemies) < MAX_ENEMIES:
        speed = min(0.5 + player_score * 0.2, max_speed)
        enemies.append(Enemy('Assets/Img/Enemies/enemy.png', screen_width, screen_height,
                             speed=speed))  # speed scales with score
        spawn_timer = random.randint(0, 60)  # randomize next spawn a bit

    for enemy in enemies[:]:
        enemy.update_position()
        if enemy.y > screen_height:
            enemies.remove(enemy)

        elif is_collision(player, enemy):
            running = False

        for bullet in player.bullets[:]:
            if is_collision(bullet, enemy):
                player.bullets.remove(bullet)
                player_score += 1
                enemies.remove(enemy)
                break

    # Draw everything
    screen.fill((25, 23, 25))
    screen.blit(background, (0, 0))
    player.display(screen)
    player.display_bullets(screen)
    for enemy in enemies:
        enemy.display(screen)
    display_score(text_x, text_y)
    pygame.display.update()
