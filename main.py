import math
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

# Score
score = 0
font = pygame.font.Font('Minecraft.ttf', 32)
textX = 10
textY = 10

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 368
playerY = 480

# Enemy
enemySprites = ['alien.png', 'alien2.png', 'alien3.png', 'alien4.png']
enemyImg = []
enemyX = []
enemyY = []
enemyDeltaMovement = [0.2, 0.2, 0.2]
enemiesNumber = 3

for i in range(enemiesNumber):
    enemyImg.append(pygame.image.load(enemySprites[random.randint(0, 3)]))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 368
bulletY = 480
bulletDeltaMovement = 0.5
# Bullet State: False for ready, True for firing
bulletState = False


# Distance operation
def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    return distance < 64


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def show_score(x, y):
    score_render = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_render, (x, y))


def fire_bullet(x, y):
    global bulletState
    bulletState = True
    screen.blit(bulletImg, (x + 24, y - 16))


# Game Loop
running = True
while running:
    # Setting background color to black
    screen.fill((0, 0, 0))

    # Vector of all inputs
    pressed = pygame.key.get_pressed()

    # Movement of the ship
    if pressed[pygame.K_LEFT] and playerX > 0:
        playerX -= 0.3
    elif pressed[pygame.K_RIGHT] and playerX < 800 - 64:
        playerX += 0.3
    if pressed[pygame.K_SPACE] and not bulletState:
        fire_bullet(playerX, bulletY)
        bulletX = playerX

    # Movement of the Enemy
    i = 0
    enemyDead = False
    while i < enemiesNumber and not enemyDead:
        if enemyX[i] >= 736:
            enemyDeltaMovement[i] = -0.2
            enemyY[i] += 10
        elif enemyX[i] <= 0:
            enemyDeltaMovement[i] = 0.2
            enemyY[i] += 10

        enemyX[i] += enemyDeltaMovement[i]
        enemy(enemyX[i], enemyY[i], i)

        # Collision Detection
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            enemiesNumber -= 1
            bulletY = 480
            bulletState = False
            score += 1
            enemyX.pop(i)
            enemyY.pop(i)
            enemyImg.pop(i)
            enemyDeltaMovement.pop(i)
            enemyDead = True

        i += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Bullet Movement
    if bulletState and bulletY <= -32:
        bulletState = False
        bulletY = 480
    elif bulletState:
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletDeltaMovement

    # Drawing Player Model
    player(playerX, playerY)

    # Showing Score on top left
    show_score(textX, textY)

    # Updating screen
    pygame.display.update()
