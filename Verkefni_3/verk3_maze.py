def mazegame():

    import pygame
    import random

    pygame.init()
    screen=pygame.display.set_mode((640,480))#640x480px
    screenrect = screen.get_rect()
    background = pygame.Surface((screen.get_size()))
    backgroundrect = background.get_rect()
    background.fill((255,255,255)) # bakgrunnur hvitur
    background = background.convert()
    background0 = background.copy()
    screen.blit(background,(0,0))

    ballsurface = pygame.Surface((10,10))
    ballsurface.set_colorkey((0,0,0))
    pygame.draw.circle(ballsurface,(255,0,0),(5,5),5) # raudur bolti
    ballsurface = ballsurface.convert_alpha()
    ballrect = ballsurface.get_rect()

    dx = 0 # delta x ... fyrir movement a x as
    dy = 0 # delta y ... movement a y as

    # -------------------- maze ----------------
    # s...thar sem spilarinn byrjar
    # n...naesta level
    # p...sidasta level
    # r...random level
    # e...end (leikurinn endar)
    # x...veggur


    #level eitt
    startlevel = ["xxx.xxxxxxxxxxxxxxxxxx",
                  ".s.....x..............",
                  "xxxx.........xx......x",
                  "x......x....x.x......x",
                  "x......x......x......x",
                  "x......x......x......x",
                  "x...xxxxxx....x......x",
                  "x......x.............x",
                  "x......x...xxxxxxxxxxx",
                  "xxxxxx.x...x.........x",
                  "x......x...x..xxxx...x",
                  "x......x......x......x",
                  "x..........xxxx...xxxx",
                  "x..........x.........x",
                  "xxxxxxxxxxxxxxxxx.xxnx"]
    # level tvo
    middlelevel =  ["xxxxxxxxxxxxxxx",
                    "xs............x",
                    "x.........x...x",
                    "x.........xp..x",
                    "x......x..x...x",
                    "x.....x...x...x",
                    "x..p.xxxxxx...x",
                    "x.....x......px",
                    "x.x....x......x",
                    "x.x.p.........x",
                    "x.x...x....p..x",
                    "x.x....x....p.x",
                    "x.xxxxxxx..n..x",
                    "x......x..p...x",
                    "x.....x.......x",
                    "xxxxxxxxxxxxxxx"]
    # smiley level
    winlevel = ["xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "xs.............................x",
                "x..............................x",
                "x..............................x",
                "x............xxx....xxx........x",
                "x...........xx.xx..xx.xx.......x",
                "x............xxx....xxx........x",
                "x..............................x",
                "x................x.............x",
                "x................x.............x",
                "x................x.............x",
                "x..............................x",
                "x................r.............x",
                "x............xx....xxx.........x",
                "x.............xxxxxxx..........x",
                "x..............................x",
                "x..............................x",
                "xxxxxxpxxxxxxxxxxxnxxxxxxxxxxxex"]


    def createblock(length, height, color):
        tmpblock = pygame.Surface((length, height))
        tmpblock.fill(color)
        tmpblock.convert()
        return tmpblock

    def addlevel(level):

        lines = len(level)
        columns = len(level[0])

        length = screenrect.width / columns
        height = screenrect.height / lines

        wallblock = createblock(length, height,(20,0,50))#veggur staerd
        nextblock = createblock(length, height,(255,50,50))#endpoint staerd
        prevblock = createblock(length, height,(255,50,255))#sprengja staerd
        endblock  = createblock(length, height,(100,100,100))#endpoint staerd
        randomblock = createblock(length, height,(0,0,200))#random kassi staerd

        background = background0.copy()

        for y in range(lines):
            for x in range(columns):
                if level[y][x] == "x": # veggur
                    background.blit(wallblock, (length * x, height * y))
                elif level[y][x] == "n": # naesta bord
                    background.blit(nextblock, (length * x, height * y))
                elif level[y][x] == "p": # sidasta bord
                    background.blit(prevblock, (length * x, height * y))
                elif level[y][x] == "r": # random bord
                    background.blit(randomblock, (length*x, height * y))
                elif level[y][x] == "e": # end kassi
                    background.blit(endblock,  (length * x, height * y))
                elif level[y][x] == "s": #start
                    ballx = length * x
                    bally = height * y
        screen.blit(background0, (0,0))

        return length, height, ballx, bally , lines, columns, background

    # listi sem heldur ollum levels
    all_levels = [startlevel, middlelevel, winlevel]
    max_levels = len(all_levels)
    my_maze = all_levels[0] # byrja a fyrsta level
    length, height,  ballx, bally, lines, columns, background = addlevel(my_maze)



    # ------------------- maze'id sjalft --------------------------


    clock = pygame.time.Clock() #pygame clock object buid til
    mainloop = True
    FPS = 60
    playtime = 0

    while mainloop:# loopan sem heldur utan um gameplay
        milliseconds = clock.tick(FPS)  # millisec sidan sidasta frame
        seconds = milliseconds / 1000.0 # sek sidan fra sidasta frame
        playtime += seconds# telur run time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # pygame gluggi lokadur af notanda
                mainloop = False
            # movement detection fyrir spilara
            elif event.type == pygame.KEYDOWN:#ef ytir
                if event.key == pygame.K_ESCAPE:#ef sleppir
                    mainloop = False
                if event.key == pygame.K_UP: # UP arrow key input
                    dy -= 1#hreyfa player up
                if event.key == pygame.K_DOWN: # DOWN arrow key input
                    dy += 1#hreyfa player nidur
                if event.key == pygame.K_RIGHT: # RIGHT arrow key input
                    dx += 1#hreyfa player til haegri
                if event.key == pygame.K_LEFT:# LEFT arrow key input
                    dx -= 1#hreyfa player til vinstri
        pygame.display.set_caption("[FPS]: %.2f dx: %i dy %i press cursor keys to move ball" % (clock.get_fps(), dx, dy))
        screen.blit(background, (0,0)) # deleta ollu
        if dx > 0:
            pointx = ballx + ballrect.width
        else:
            pointx = ballx
        if dy > 0:
            pointy = bally + ballrect.height
        else:
            pointy = bally
        # ------- finna ut ef boltinn aetlar i gegnum veggi
        if pointx + dx < 0:
            ballx = 0
            pointx = 0
            dx = 0
        elif pointx + dx > screenrect.width:
            ballx = screenrect.width - ballrect.width
            pointx = screenrect.width - ballrect.width
            dx = 0
        if pointy + dy < 0:
            bally = 0
            pointy = 0
            dy = 0
        elif pointy + dy > screenrect.height:
            bally = screenrect.height - ballrect.height
            pointy = screenrect.height - ballrect.height
            dy = 0
        y1 = int(pointy/height)
        y1 = max(0,y1) # aldrei minna en 1
        y1 = min(y1,lines-1) # aldrei staerra en linurnar
        x1 = int((pointx + dx)/length)
        x1 = max(0,x1) # aldrei minna en 0
        x1 = min(x1,columns-1)
        y2 = int((pointy+dy)/height)
        y2 = max(0,y2)
        y2 = min(y2,lines-1)
        # -------------- athuga hvada tegund af golfi spilarinn er a ------
        if my_maze[y1][x1] == "x":
            dx = 0
        else:
            ballx += dx
        if my_maze[y2][x1] == "x":
            dy = 0
        else:
            bally += dy
        # ---------------hreyfa bolta
        screen.blit(ballsurface, (ballx, bally))
        # -------------- athuga "special tile" s.s. sprengjur, gildrur etc.
        bline = int(bally / height) # bolta linan sem hann er a
        bcolumn = int(ballx / length) # bolta column sem hann er a
        if my_maze[bline][bcolumn] == "n":#ef spilari fer a naesta level kassann
           actual = all_levels.index(my_maze)
           my_maze = all_levels[(actual + 1) % max_levels]
           length, height,  ballx, bally,  lines, columns,background = addlevel(my_maze)
        elif my_maze[bline][bcolumn] == "p":# ef spilari fer a sidasta level kassann
            actual = all_levels.index(my_maze)
            my_maze = all_levels[(max_levels + actual - 1) % max_levels]
            length, height,  ballx, bally,  lines, columns,background = addlevel(my_maze)
        elif my_maze[bline][bcolumn] == "r":# ef spilari fer a random level kassann
            my_maze = random.choice(all_levels)
            length, height,  ballx, bally,  lines, columns,background = addlevel(my_maze)
        elif my_maze[bline][bcolumn] == "e":#ef spilari fer a end kassann
            # leikur unninn, fara ur mainloop
            print("---*** congratulation, you escaped the maze ! ***-------")
            mainloop = False
        pygame.display.flip()
    print("This maze game was played for {:.2f} seconds".format(playtime))#printar tima spiladan i console
if __name__ == "__main__":
    mazegame()

