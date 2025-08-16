import pygame
pygame.init() # Initialize pygame

# Create the screen (width, height)
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('img/logo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('img/player.png')
playerX = 370
playerY = 480

def player():
    # Draw the player
    # blit means draw
    screen.blit(playerImg, (playerX, playerY))

# Game Loop
running = True
while running:
    # Event to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Change background color
    screen.fill((25, 23, 25))

    # Call player in while loop so it appears on every frame
    player()

    # Update Screen
    pygame.display.update()