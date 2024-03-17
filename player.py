import pygame
from consts import *
class Player:

    def __init__(self, x, y, width, height, velocity):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.velocity = velocity
        self.player = pygame.image.load("./player/player.png")
        self.rect = self.player.get_rect()
        self.isOnPlatform = True
        self.isJumping = False
        self.jumpCount = 8
        self.score = 0
        self.isFalling = False
        self.isLeft = False
        self.isRight = False
        self.HP = 3

    def movement(self, window):
        keys = pygame.key.get_pressed()

        if self.isJumping  :
                if self.jumpCount >= -8 :
                    self.y -= (self.jumpCount * abs(self.jumpCount)) * 1
                    self.jumpCount -= 1
                    if self.jumpCount < 0:
                        if self.isLeft:
                            self.player = pygame.image.load("./player/jumpDownl.png")
                        else:
                            self.player = pygame.image.load("./player/jumpDownr.png")
                    else: 
                        if self.isLeft:
                            self.player = pygame.image.load("./player/jumpUpl.png")
                        else:
                            self.player = pygame.image.load("./player/jumpUpr.png")
                else:
                    self.jumpCount = 8  
                    self.isJumping = False
        else:
            self.player = pygame.image.load("./player/player.png")


        # shifting player's y coordinate to align him with platform
        if self.score > 1 and self.score < 30 :
            self.y += 5
        elif self.score >= 30 and self.score < 60 :
            self.y += 6
        elif self.score >= 60 and self.score < 100 :
            self.y += 7
        elif self.score >= 100 :
            self.y += 8

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.x > self.velocity:
            self.player = pygame.image.load("./player/l1.png")
            self.isLeft = True
            self.isRight = False
            self.x -= self.velocity

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT])  and self.x < window.get_width() - self.width - self.velocity :
            self.player = pygame.image.load("./player/r1.png")
            self.isRight = True
            self.isLeft = False
            self.x += self.velocity

        # gravity - bugged
        if not self.isOnPlatform and not self.isJumping :
            self.y += self.velocity * 2
            self.isFalling = True
        else:
            self.isFalling = False 

                

    def handlePlatforms(self,platform_group, window):
        platform_group.draw(window)

        if self.isFalling :
            if self.isLeft:
                self.player = pygame.image.load("./player/jumpDownl.png")
            else:
                self.player = pygame.image.load("./player/jumpDownr.png")
            for platform in platform_group : 
                if self.rect.colliderect(platform.rect) :
                    if round(self.rect.centery)  < round(platform.rect.top) :
                            
                            self.jumpCount = 8
                            self.isJumping = False
                            if not self.isJumping :
                                self.y = platform.rect.top - self.height 
                                self.isOnPlatform = True
                                self.score+=1
                else :
                    self.isOnPlatform = False
        else : 
            for platform in platform_group : 
                if self.rect.colliderect(platform.rect) :
                    if round(self.rect.centery)  < round(platform.rect.top) and self.jumpCount <= 0 :
                            
                            self.jumpCount = 8
                            self.isJumping = False
                            if not self.isJumping :
                                self.y = platform.rect.top - self.height 
                                self.isOnPlatform = True
                                self.score+=1
                else :
                    self.isOnPlatform = False

        for platform in platform_group : 
            if round(self.y) == round(platform.rect.top) - self.height and round(self.rect.right) >= round(platform.rect.left) and round(self.rect.left) <= round(platform.rect.right):
                self.isOnPlatform = True
                self.y = platform.rect.top - self.height

    def drawPlayer(self, window) :
        window.blit(self.player , (self.x , self.y))
        self.rect.update(self.x, self.y, self.width, self.height)
        self.rect.y = self.y
        self.rect.x = self.x


    def jumpSound(self,jumpSound) :
        if self.isOnPlatform or self.y == MAX_HEIGHT - self.height :
            jumpSound.play() 


    def setHighestScore(self) :

        with open('./highestScore.txt', 'r') as file:
            highestScore = int(file.readline())

        if self.score > highestScore : 
            with open('./highestScore.txt', 'w') as file:
                file.write(str(self.score))


    def handlePlayerHP(self,window) :
        greyHeart = pygame.image.load("./assets/greyHeart.png")
        redHeart = pygame.image.load("./assets/redHeart.png")
        scaledGreyHeart = pygame.transform.scale(greyHeart, (60,60))
        scaledRedHeart = pygame.transform.scale(redHeart, (60,60))

        if self.HP >= 1 :
            window.blit(scaledRedHeart, (450,720))
        else :
            window.blit(scaledGreyHeart, (450,720))

        if self.HP >= 2 :
            window.blit(scaledRedHeart, (510,720))
        else :
            window.blit(scaledGreyHeart, (510,720))

        if self.HP == 3 :
            window.blit(scaledRedHeart, (570,720))
        else :
            window.blit(scaledGreyHeart, (570,720))


    


