import pygame
import random

pygame.init()
font = pygame.font.SysFont('Arial', 25)

width = 620
height = 250

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

LEFT_BUTTON = 1

# cubes
dice1 = pygame.image.load("images/sd1.png")
dice2 = pygame.image.load("images/sd2.png")
dice3 = pygame.image.load("images/sd3.png")
dice4 = pygame.image.load("images/sd4.png")
dice5 = pygame.image.load("images/sd5.png")
dice6 = pygame.image.load("images/sd6.png")

# set cubes to array
dice = [dice1, dice2, dice3, dice4, dice5, dice6]
rethrow = list()

# cubes sizes
dice_len, dice_height = dice1.get_rect().size
screen = pygame.display.set_mode((width, height))

dice_list = list()

rethrow_bt = pygame.Rect(20, 120, 150, 50)

# random dice
for x in xrange(0, 5):
    dice_list.append(random.randint(0, 5))

x = 10
y = 10
rethrowCount = 0

running = True

# while
while running:
    event = pygame.event.poll()
    # if pygame = quit stop game
    if event.type == pygame.QUIT:
        running = False

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
        for x in xrange(0, len(dice_list)):
            if dice_list[x].collidepoint(event.pos):
                rethrow.append(x)
        if rethrow_bt.collidepoint(event.pos):
            if rethrowCount < 2:
                for x in xrange(0, len(rethrow)):
                    dice_list[rethrow[x]] = random.randint(1, 6)
                rethrowCount = rethrowCount + 1

    # sets screen to white
    screen.fill(white)
    pygame.draw.rect(screen, blue, rethrow_bt)
    x = 10
    y = 10

    # cubes
    for a in xrange(0, len(dice_list)):
        screen.blit(dice[dice_list[a]], (x, y))
        x = x + dice_len

    pygame.display.update()
