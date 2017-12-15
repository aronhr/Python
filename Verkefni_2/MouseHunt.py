import pygame
import random
import time

pygame.init()
font = pygame.font.SysFont('Arial', 15)

width = 400
height = 150
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
color = 0
LEFT_BUTTON = 1
rects = list()
rect_colors = list()
screen = pygame.display.set_mode((width, height))

# position for boxes
x = 10
y = 10
size = 30

for a in xrange(0, 7):
    rects.append(pygame.Rect(x, y, size, size))
    x = x + (size + 5)

# position for boxes
x = 10
y = 45
for a in xrange(0, 7):
    rects.append(pygame.Rect(x, y, size, size))
    x = x + (size + 5)

# nullstillir
catsHit = 0
miceHit = 0
nullHit = 0

# red = cat
# blue = mouse
running = True
while running:
    # makes screen white
    screen.fill(white)
    event = pygame.event.poll()

    # Writes text on app
    screen.blit(font.render('Click on the blue boxes', True, (0, 0, 0)), (10, 80))
    screen.blit(font.render('Red = cat. Don\'t click them', True, (0, 0, 0,)), (10, 95))
    screen.blit(font.render('Blue = mouse.', True, (0, 0, 0)), (10, 110))

    # when game is quit stats prints out
    if event.type == pygame.QUIT:
        print('Mice hit = ' + str(miceHit))
        print('Cats hit = ' + str(catsHit))
        print('Other hit= ' + str(nullHit))
        running = False
    # Check what color user clicked on
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
        for x in xrange(0, len(rects)):
            if rects[x].collidepoint(event.pos):
                if rect_colors[x] == 'Red':
                    catsHit = catsHit = 1
                elif rect_colors[x] == 'Blue':
                    miceHit = miceHit + 1
                else:
                    nullHit = nullHit + 1

    rect_colors = list()

    # draws random colors in App
    for x in xrange(0, len(rects)):
        color = random.randint(1, 3)
        if color == 2:
            pygame.draw.rect(screen, red, rects[x])
            rect_colors.append('Red')
        elif color == 1:
            pygame.draw.rect(screen, blue, rects[x])
            rect_colors.append('Blue')
        else:
            rect_colors.append('None')
    time.sleep(0.2)  # Wait time after one round

    # Update screen
    pygame.display.update()
