import pygame
pygame.init() # Initialize pygame

# Create the screen (height,width)
screen = pygame.display.set_mode((800, 600))

# Game Loop
running = True
while running:
    # Event to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
