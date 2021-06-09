import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('laser-gun.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 368
playerY = 480


def player():
    screen.blit(playerImg, (playerX, playerY))


# Game Loop
running = True
while running:
    # Setting background color to white
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing Player Model
    player()

    # Updating screen
    pygame.display.update()

