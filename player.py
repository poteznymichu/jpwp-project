import pygame
from consts import *
class Player:

    def __init__(self, x, y, width, height, velocity):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.velocity = velocity
        self.player = pygame.image.load("./assets/player.jpg")
        self.rect = self.player.get_rect()
        self.isOnPlatform = True
        self.isJumping = False
        self.jumpCount = 8
        self.score = 0

    def movement(self, window):

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.x > self.velocity:
            self.x -= self.velocity

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT])  and self.x < window.get_width() - self.width - self.velocity :
            self.x += self.velocity

        if self.isJumping  :
            if self.jumpCount >= -8 :
                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.8
                self.jumpCount -= 1
            else:
                self.jumpCount = 8  
                self.isJumping = False
                

    def handlePlatforms(self,platform_group, window):
        platform_group.draw(window)

        for platform in platform_group : 

            if self.rect.colliderect(platform.rect) :
                if self.rect.centery  < platform.rect.top and self.jumpCount <= 0 :

                        self.jumpCount = 8
                        self.isJumping = False
                        if not self.isJumping :
                            self.y = platform.rect.top - self.height 
                            self.isOnPlatform = True
            else :
                self.isOnPlatform = False

        for platform in platform_group : 
            if self.y == platform.rect.top - self.height and self.rect.right >= platform.rect.left and self.rect.left <= platform.rect.right:
                self.isOnPlatform = True
                self.y = platform.rect.top - self.height

    def handleGravity(self, gravity):

        if not self.isOnPlatform and not self.isJumping : 
                self.y += gravity ** 2   
                self.jumpCount = -9

    def jumpSound(self,jumpSound) :
        if self.isOnPlatform or self.y == MAX_HEIGHT - self.height :
            jumpSound.play() 

    def setScore(self, platformGroup, visitedPlatforms) :

        for platform in platformGroup :
            if self.y == platform.rect.top - self.height :
                if platform.rect.top not in visitedPlatforms :
                    self.score += 1
                    visitedPlatforms.append(platform.rect.top) 
        self.setHighestScore()
  
    def setHighestScore(self) :

        with open('./highestScore.txt', 'r') as file:
            highestScore = int(file.readline())

        if self.score > highestScore : 
            with open('./highestScore.txt', 'w') as file:
                file.write(str(self.score))


    def drawPlayer(self, window) :
        window.blit(self.player , (self.x , self.y))
        self.rect.update(self.x, self.y, self.width, self.height)

