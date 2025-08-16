import pygame
pygame.init() # Initialize pygame

# Create the screen (height,width)
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('img/logo.png')
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    # Event to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Change background color
    screen.fill((25, 23, 25))

    # Update Screen
    pygame.display.update()