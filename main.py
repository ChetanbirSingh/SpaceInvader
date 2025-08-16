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
mixer.music.play(-1)

player = Player('Assets/Img/player.png', 370, 580, screen_width, screen_height)

enemies = []
spawn_timer = 0
spawn_interval = 120
MAX_ENEMIES = 8
max_speed = 2.5

font = pygame.font.Font('freesansbold.ttf', 32)

def display_score():
    score = font.render("Score: " + str(player_score), True, (255, 255, 255))
    screen.blit(score, (10, 10))


def game_over_screen():
    text = font.render("GAME OVER - Press R to Restart", True, (255, 0, 0))
    # Center the text on the screen
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    # Draw the text
    screen.fill((0, 0, 0))  # optional: clear screen or keep background
    screen.blit(text, text_rect)
    pygame.display.update()  # show it

    while True:
        mixer.music.pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # restart the game

def is_collision(sprite1, sprite2):
    distance = math.sqrt((sprite1.x - sprite2.x) ** 2 + (sprite1.y - sprite2.y) ** 2)
    return distance < 27


def reset_game():
    global player, enemies, player_score, spawn_timer
    player.x = 370
    player.y = 580
    player.bullets.clear()
    enemies.clear()
    player_score = 0
    spawn_timer = 0
    mixer.music.unpause()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.handle_input(event)

    player.update_position()
    player.update_bullets()

    # Spawn enemies randomly
    spawn_timer += 1
    if spawn_timer >= spawn_interval and len(enemies) < MAX_ENEMIES:
        speed = min(0.5 + player_score * 0.2, max_speed)
        enemies.append(Enemy('Assets/Img/Enemies/enemy.png', screen_width, screen_height, speed=speed))
        spawn_timer = random.randint(0, 60)

    # Update enemies and check collisions
    for enemy in enemies[:]:
        enemy.update_position()
        if enemy.y > screen_height:
            enemies.remove(enemy)

        elif is_collision(player, enemy):
            if game_over_screen():  # Show game over and wait for restart
                reset_game()
                break  # exit enemy loop to restart properly

        for bullet in player.bullets[:]:
            if is_collision(bullet, enemy):
                player.bullets.remove(bullet)
                player_score += 1
                enemies.remove(enemy)
                mixer.Sound('Assets/Audio/explosion.wav').play()
                break

    # Draw everything
    screen.fill((25, 23, 25))
    screen.blit(background, (0, 0))
    player.display(screen)
    player.display_bullets(screen)
    for enemy in enemies:
        enemy.display(screen)
    display_score()
    pygame.display.update()
