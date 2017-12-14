import pygame
import random

pygame.init()
font = pygame.font.SysFont('Arial', 25)


# dice for both computer and player
def diceing():
    for x in xrange(0, 5):
        comp_dice.append(random.randint(1, 6))
        user_dice.append(random.randint(1, 6))


# check who wins the round
def findWinner():
    going = True
    if sum(comp_dice) > sum(user_dice):
        print("Computer wins")
    elif sum(comp_dice) < sum(user_dice):
        print("You win")
    else:
        print("Draw")

    # while loop
    while going:
        # updates the screen
        pygame.display.update()
        event = pygame.event.poll()

        x = 10
        y = 10

        # draw computer dice
        for a in xrange(0, len(comp_dice)):
            screen.blit(dice[comp_dice[a] - 1], (x, y))
            x = x + dice_len

        y = y + dice_height
        x = 10

        # draw user dice
        for a in xrange(0, len(user_dice)):
            screen.blit(dice[user_dice[a] - 1], (x, y))
            x = x + dice_len
        if event.type == pygame.QUIT:
            going = False

# throws one cube
def throwOne():
    user_dice[4] = random.randint(1, 6)
    findWinner()


# throws all cubes
def throwAll():
    for x in xrange(0, 5):
        user_dice = list()
        user_dice.append(random.randint(1, 6))
    findWinner()


# size of app
width = 550
height = 350

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

LEFT_BUTTON = 1

# loads the cubes
dice1 = pygame.image.load("images/sd1.png")
dice2 = pygame.image.load("images/sd2.png")
dice3 = pygame.image.load("images/sd3.png")
dice4 = pygame.image.load("images/sd4.png")
dice5 = pygame.image.load("images/sd5.png")
dice6 = pygame.image.load("images/sd6.png")

# size of the cubes
dice_len, dice_height = dice1.get_rect().size
screen = pygame.display.set_mode((width, height))

# array of cubes
dice = [dice1, dice2, dice3, dice4, dice5, dice6]

comp_dice = list()
user_dice = list()

# Title of app
pygame.display.set_caption("Teningaspil")

# throws cubes
diceing()

# buttons
rectA = pygame.Rect(45, 250, 100, 40)
rectB = pygame.Rect(160, 250, 100, 40)
rectC = pygame.Rect(270, 250, 100, 40)

running = True
while running:
    x = 10
    y = 10
    event = pygame.event.poll()

    # Press button A
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
        if rectA.collidepoint(event.pos):
            throwOne()
            running = False

        # press button B
        if rectB.collidepoint(event.pos):
            throwAll()
            running = False

        # press button c
        if rectC.collidepoint(event.pos):  # TODO: Fix play again button
            diceing()
            running = True
    elif event.type == pygame.QUIT:
        running = False
        break

    # set screen to white
    screen.fill(white)

    x = 10
    y = 10

    # render buttons
    pygame.draw.rect(screen, red, rectA)
    screen.blit(font.render('Throw one', True, (0, 0, 0)), (45, 250))
    pygame.draw.rect(screen, red, rectB)
    screen.blit(font.render('Throw all', True, (0, 0, 0)), (160, 250))
    pygame.draw.rect(screen, blue, rectC)
    screen.blit(font.render('Play again', True, (0, 0, 0)), (270, 250))

    # render computer dice
    for a in xrange(0, len(comp_dice)):
        screen.blit(dice[comp_dice[a] - 1], (x, y))
        x = x + dice_len

    y = y + dice_height
    x = 10

    # render user dice
    for a in xrange(0, len(user_dice) - 1):
        screen.blit(dice[user_dice[a] - 1], (x, y))
        x = x + dice_len

    screen.blit(dice[random.randint(0, 5)], (x, y))
    pygame.display.update()

pygame.quit()
