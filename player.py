import pygame
from consts import *
class Player:

    def __init__(self, x, y, width, height, vel, platformGroup):
        self.x = x
        self.width = width
        self.height = height
        self.y = MAX_HEIGHT - self.height
        self.vel = vel
        self.platformGroup = platformGroup
        self.player = pygame.image.load("./assets/player.jpg")
        self.rect = self.player.get_rect()
        self.isOnPlatform = False
        self.isJump = False
        self.jumpCount = 8
        

    def movement(self, windowWidth):

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.x > self.vel:
            self.x -= self.vel

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT])  and self.x < windowWidth - self.width - self.vel:
            self.x += self.vel


        if self.isJump  :
            if self.jumpCount >= -8 :
                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.8
                self.jumpCount -= 1
            else:
                self.jumpCount = 8  
                self.isJump = False
                
        gravity = 3.5
        if not self.isOnPlatform and not self.isJump : 
            if self.y < MAX_HEIGHT - self.height: 
                self.y +=gravity ** 2   
                self.jumpCount = -9
                
        for platform in self.platformGroup : 

            if self.rect.colliderect(platform.rect) :

                if self.rect.centery  <= platform.rect.top  :
                        self.jumpCount = 8

                        self.isJump = False
                        if not self.isJump :
                            self.y = platform.rect.top - self.height               
            else :
                self.isOnPlatform = False
                

        for platform in self.platformGroup : 
            if self.y == platform.rect.top - self.height and self.rect.right >= platform.rect.left and self.rect.left <= platform.rect.right:
                self.isOnPlatform = True


        if self.y > MAX_HEIGHT-self.height : 
            self.y = MAX_HEIGHT-self.height
            self.jumpCount = 8
            self.isJump = False


  
    def drawPlayer(self, window) :
        window.blit(self.player , (self.x , self.y))
        self.rect.update(self.x, self.y, self.width, self.height)
