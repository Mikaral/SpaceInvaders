import random
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

# Enemy
enemyImg = pygame.image.load('rodrigo.png')
enemyX = random.randint(0, 800 - 64)
enemyY = random.randint(50, 150)
enemyDeltaMovement = 0.1


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
running = True
while running:
    # Setting background color to white
    screen.fill((0, 0, 0))

    # Vector of all inputs
    pressed = pygame.key.get_pressed()

    # Movement of the ship
    if pressed[pygame.K_LEFT] and playerX > 0:
        playerX -= 0.2
    elif pressed[pygame.K_RIGHT] and playerX < 800 - 64:
        playerX += 0.2

    # Movement of the Enemy
    if enemyX >= 800 - 64:
        enemyDeltaMovement = -0.1
    elif enemyX <= 0:
        enemyDeltaMovement = 0.1

    enemyX += enemyDeltaMovement
    enemyY += 0.001

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing Player Model
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    # Updating screen
    pygame.display.update()
