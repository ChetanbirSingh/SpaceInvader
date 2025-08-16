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
playerX_velocity = 0

speed = 0.2

def player(x, y):
    # Draw the player
    # blit means draw
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:
    # Event to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed
        # KEYDOWN = fired ONCE when key is first pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Instead of moving once, set a "velocity"
                # This makes player move continuously each frame
                playerX_velocity -= speed
            elif event.key == pygame.K_RIGHT:
                playerX_velocity += speed

        # If keystroke has been released
        elif event.type == pygame.KEYUP:
            playerX_velocity = 0

    # Move the player
    # Update player position by its change value
    # This runs every frame (~60 times per second),
    # so the player moves smoothly while the key is held
    playerX += playerX_velocity

    # Prevent the player from moving off the left edge
    if playerX <= 0:
        playerX = 0
    # Prevent the player from moving off the right edge
    elif playerX > 800 - playerImg.get_width():
        playerX = 800 - playerImg.get_width()

    # Change background color
    screen.fill((25, 23, 25))

    # Call player in while loop so it appears on every frame
    player(playerX, playerY)

    # Update Screen
    pygame.display.update()