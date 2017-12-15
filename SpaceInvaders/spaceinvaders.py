import pygame
from pygame.locals import *
import sys
import random

class SpaceInvaders:

    def __init__(self):
        self.score = 0
        self.lives = 2
        pygame.font.init()
        self.font = pygame.font.Font("assets/font.ttf", 15)

        self.screen = pygame.display.set_mode((800, 600))
        self.enemySprites = {
                0:[pygame.transform.scale(pygame.image.load("assets/alien10.png").convert(), (64,64)), pygame.transform.scale(pygame.image.load("assets/alien11.png").convert(), (64,64))],
                1:[pygame.transform.scale(pygame.image.load("assets/alien20.png").convert(), (64,64)), pygame.transform.scale(pygame.image.load("assets/alien21.png").convert(), (64,64))],
                2:[pygame.transform.scale(pygame.image.load("assets/alien30.png").convert(), (64,64)), pygame.transform.scale(pygame.image.load("assets/alien31.png").convert(), (64,64))],
                }
        self.background = pygame.transform.scale(pygame.image.load("assets/space.png").convert(), (800, 600))
        self.blackShip = pygame.transform.scale(pygame.image.load("assets/blackship.png").convert(), (50, 50))
        #Stadsetning a black ship
        self.blackShipX = 50
        self.blackShipY = 50
        self.blackShipVisible = False
        #myndir fyrir leikmann, thegar hann snyr upp,nidur,vinstri,haegri
        self.shooterImageUp = pygame.transform.scale(pygame.image.load("assets/shooter.png").convert(), (50, 70))
        self.shooterImageLeft = pygame.transform.rotate(self.shooterImageUp,90)
        self.shooterImageRight = pygame.transform.rotate(self.shooterImageUp,-90)
        self.shooterImageDown = pygame.transform.rotate(self.shooterImageUp,180)
        #leikmadur byrjar a thvi ad snua upp
        self.player = self.shooterImageUp
        self.animationOn = 0
        #attin sem geimverur fara i
        self.direction = 1
        self.enemySpeed = 20
        self.lastEnemyMove = 0
        #stadsetning leikmanns
        self.playerX = 400
        self.playerY = 520
        #true ef black ship er synilegt og leikmadur ytir a t
        self.shield = False
        self.bullet = None
        self.pause = False
        # 0=up 1=right 2=down 3=left
        self.bulletDirection = 0
        #skot fra ovinum
        self.bullets = []
        self.enemies = []
        self.deadEnemies = 0
        startY = 50
        startX = 50
        #thetta byr til ovinina
        for rows in range(6):
            out = []
            if rows < 2:
                enemy = 0
            elif rows < 4:
                enemy = 1
            else:
                enemy = 2
            for columns in range(10):
                out.append((enemy,pygame.Rect(startX * columns, startY * rows, 35, 35)))
            self.enemies.append(out)
        self.chance = 990
    #kallad i thetta til ad uppfaera stodu ovina
    def enemyUpdate(self):
        if not self.lastEnemyMove:
            for enemy in self.enemies:
                for enemy in enemy:
                    enemy = enemy[1]
                    if enemy.colliderect(pygame.Rect(self.playerX, self.playerY, self.player.get_width(), self.player.get_height())):
                        self.lives -= 1
                        self.resetPlayer()
                    enemy.x += self.enemySpeed * self.direction
                    self.lastEnemyMove = 25
                    if enemy.x >= 750 or enemy.x <= 0:
                        self.moveEnemiesDown()
                        self.direction *= -1
                    
                    chance = random.randint(0, 1000)
                    if chance > self.chance:
                        self.bullets.append(pygame.Rect(enemy.x, enemy.y, 5, 10))
                        self.score += 5
            if self.animationOn:
                self.animationOn -= 1                                                                                                                                                        
            else:
                self.animationOn += 1
        else:
            self.lastEnemyMove -= 1
    
    #allir ovinir fluttir um tuttugu px nidur
    def moveEnemiesDown(self):
        for enemy in self.enemies:
            for enemy in enemy:
                enemy = enemy[1]
                enemy.y += 20

    #thetta er til ad uppfaera leikmann og taka a thegar ytt hefur verid a einhverja takka
    def playerUpdate(self):
        key = pygame.key.get_pressed()

        if key[K_p]:
            self.pause = not self.pause
        elif key[K_t] and self.blackShipVisible:
            self.shield = True

        elif key[K_RIGHT] and self.playerX < 800 - self.player.get_width():
            if self.player != self.shooterImageRight:
                self.player = self.shooterImageRight
            self.playerX += 5
        elif key[K_LEFT] and self.playerX > 0:
            if self.player != self.shooterImageLeft:
                self.player = self.shooterImageLeft
            self.playerX -= 5
        elif key[K_UP] and self.playerY >= 35:
            if self.player != self.shooterImageUp:
                self.player = self.shooterImageUp
            self.playerY -= 5
        elif key[K_DOWN] and self.playerY < 545:
            if self.player != self.shooterImageDown:
                self.player = self.shooterImageDown
            self.playerY += 5
        elif key[K_SPACE] and not self.bullet and not self.blackShipVisible:
            if self.player == self.shooterImageRight:
                # shoot right
                self.bulletDirection = 1
                self.bullet = pygame.Rect(self.playerX + self.player.get_width() / 2 - 5, self.playerY + self.player.get_height() / 2 - 2, 10, 5)
            if self.player == self.shooterImageLeft:
                # shoot left
                self.bulletDirection = 3
                self.bullet = pygame.Rect(self.playerX + self.player.get_width() / 2 + 5, self.playerY + self.player.get_height() / 2 - 2, 10, 5)
            if self.player == self.shooterImageUp:
                # shoot up
                self.bulletDirection = 0
                self.bullet = pygame.Rect(self.playerX + self.player.get_width() / 2 - 2, self.playerY - 15, 5, 10)
            if self.player == self.shooterImageDown:
                # shoot down
                self.bulletDirection = 2
                self.bullet = pygame.Rect(self.playerX + self.player.get_width() / 2- 2, self.playerY + 15, 5, 10)
    #tharna er verid ad uppfaera black ship og drepa ovini sem blackshit hefur keyrt a
    def blackShipUpdate(self):
        for i, enemyx in enumerate(self.enemies):
            for j, enemy in enumerate(enemyx):
                enemy = enemy[1]
                if self.blackShip and enemy.colliderect(pygame.Rect((self.blackShipX, self.blackShipY), (self.blackShip.get_width(), self.blackShip.get_height()))):
                    self.enemies[i].pop(j)
        #thetta thidir ad spilarinn rekst a black ship
        if pygame.Rect((self.playerX, self.playerY), (self.player.get_width(), self.player.get_height())).colliderect(pygame.Rect((self.blackShipX, self.blackShipY), (self.blackShip.get_width(), self.blackShip.get_height()))):
            self.deadEnemies = 0
            self.blackShipVisible = False
            if self.shield:
                self.shield = False
            elif not self.shield:
                self.lives = 0

        if (self.playerX + self.player.get_width() / 2) > (self.blackShipX + self.blackShip.get_width() / 2):
            self.blackShipX += 1
        elif (self.playerX + self.player.get_width() / 2) < (self.blackShipX + self.blackShip.get_width() / 2):
            self.blackShipX -= 1
        if (self.playerY + self.player.get_height() / 2) > (self.blackShipY + self.blackShip.get_height() / 2):
            self.blackShipY += 1
        elif (self.playerY + self.player.get_width() / 2) < (self.blackShipY + self.blackShip.get_width() / 2):
            self.blackShipY -= 1

    #thetta er byssukula sem leikmadur hefur skotid
    def bulletUpdate(self):
        for i, enemy in enumerate(self.enemies):
            for j, enemy in enumerate(enemy):
                enemy = enemy[1]
                if self.bullet and enemy.colliderect(self.bullet):
                    self.enemies[i].pop(j)
                    self.deadEnemies += 1
                    if self.deadEnemies == 10:
                        self.blackShipVisible = True
                    self.bullet = None
                    self.chance -= 1
                    self.score += 100
                
        if self.bullet:
            if self.bulletDirection == 0:
                self.bullet.y -= 20
                if self.bullet.y < 0:
                    self.bullet = None
            if self.bulletDirection == 1:
                self.bullet.x += 20
                if self.bullet.x > 800:
                    self.bullet = None
            if self.bulletDirection == 2:
                self.bullet.y += 20
                if self.bullet.y > 600:
                    self.bullet = None
            if self.bulletDirection == 3:
                self.bullet.x -= 20
                if self.bullet.x < 0:
                    self.bullet = None

        #bysssukulur sem ad ovinir hafa skotid
        for x in self.bullets:
            x.y += 20
            if x.y > 600:
                self.bullets.remove(x)
            if x.colliderect(pygame.Rect(self.playerX, self.playerY, self.player.get_width(), self.player.get_height())):
                self.lives -= 1
                self.bullets.remove(x)
                self.resetPlayer()
    #faerir leikmann i midju
    def resetPlayer(self):
        self.playerX = 400

    #thetta er adgerd thar sem vid teiknum alla hluti i leiknum
    def run(self):
        clock = pygame.time.Clock()
        for x in range(3):
            self.moveEnemiesDown()
        while True:
            clock.tick(60)
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background,(0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            for enemy in self.enemies:
                for enemy in enemy:
                    self.screen.blit(pygame.transform.scale(self.enemySprites[enemy[0]][self.animationOn], (35,35)), (enemy[1].x, enemy[1].y))

            if self.shield:
                pygame.draw.circle(self.screen, (0, 0, 255), (self.playerX + self.player.get_width() / 2 , self.playerY  + self.player.get_height() / 2 ), 50, 3)
                self.screen.blit(self.player, (self.playerX, self.playerY))
            elif not self.shield:
                self.screen.blit(self.player, (self.playerX, self.playerY))

            if self.blackShipVisible:
                self.screen.blit(self.blackShip, (self.blackShipX, self.blackShipY))

            if self.bullet:
                pygame.draw.rect(self.screen, (255, 255, 0), self.bullet)
            for bullet in self.bullets:
                pygame.draw.rect(self.screen, (255,255,255), bullet)

            if not self.enemies:
                self.screen.blit(pygame.font.Font("assets/space_invaders.ttf", 100).render("You Win!", -1, (52,255,0)), (100, 200))
            elif self.lives > 0:
                if self.blackShipVisible:
                    self.blackShipUpdate()
                self.bulletUpdate()
                self.enemyUpdate()
                self.playerUpdate()
            elif self.lives == 0:
                self.screen.blit(pygame.font.Font("assets/space_invaders.ttf", 100).render("You Lose!", -1, (52,255,0)), (100, 200))
            self.screen.blit(self.font.render("Lives: {}".format(self.lives), -1, (255,255,255)), (20, 10))
            self.screen.blit(self.font.render("Score: {}".format(self.score), -1, (255,255,255)), (400, 10))
            pygame.display.flip()

#thetta er keyrslu adgerdin
if __name__ == "__main__":
    SpaceInvaders().run()
