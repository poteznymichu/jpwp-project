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
        self.isOnPlatform = False
        self.isJumping = False
        self.jumpCount = 8
        self.score = 0


    def movement(self, window):

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.x > self.velocity:
            self.x -= self.velocity

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT])  and self.x < window.get_width() - self.width - self.velocity:
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

                if self.rect.centery  <= platform.rect.top and self.jumpCount <= 0 :
                        
                        self.jumpCount = 8
                        self.isJumping = False
                        if not self.isJumping :
                            self.y = platform.rect.top - self.height               
            else :
                self.isOnPlatform = False

        for platform in platform_group : 
            if self.y == platform.rect.top - self.height and self.rect.right >= platform.rect.left and self.rect.left <= platform.rect.right:
                self.isOnPlatform = True


    def handleGravity(self, gravity):

        if not self.isOnPlatform and not self.isJumping : 
            if self.y < MAX_HEIGHT - self.height: 
                self.y += gravity ** 2   
                self.jumpCount = -9

        if self.y > MAX_HEIGHT-self.height : 
            self.y = MAX_HEIGHT-self.height
            self.jumpCount = 8
            self.isJumping = False


    def jumpSound(self,jumpSound) :
        if self.isOnPlatform or self.y == MAX_HEIGHT - self.height :
            jumpSound.play() 
  

    def drawPlayer(self, window) :
        window.blit(self.player , (self.x , self.y))
        self.rect.update(self.x, self.y, self.width, self.height)
