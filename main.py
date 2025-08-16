import pygame
from Entities.player import Player

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('img/logo.png')

pygame.display.set_icon(icon)

# Create player instance
player = Player(img_path='img/player.png', x=370, y=480, screen_width=screen_width, screen_height=screen_height)

running = True
while running:
    # Process all events (keyboard, mouse, window close, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the game loop when the window is closed
        player.handle_input(event)  # Update player velocity based on key events

    # Update game state
    player.update_position()  # Move the player according to current velocity

    # Render the frame
    screen.fill((25, 23, 25))
    player.display(screen)     # Draw the player on the screen
    pygame.display.update()    # Refresh the display with the new frame
