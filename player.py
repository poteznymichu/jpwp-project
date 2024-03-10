import pygame
from consts import *
class Player:

    def __init__(self, x, y, width, height, vel, platformGroup):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
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
        
        if not(self.isJump)  and  keys[pygame.K_SPACE]:
            self.isJump = True
            self.didJump = True

        if self.isJump :

            if self.jumpCount >= -8 :
                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5 + self.jumpCount
                self.jumpCount -= 1
            else:
                self.jumpCount = 8  
                self.isJump = False
                self.didJump = False


        gravity = 3.5
        if self.y < MAX_HEIGHT-PLAYER_HEIGHT and not(self.isJump) and not(self.isOnPlatform):
            self.jumpCount = -9
            self.y += gravity ** 2
            gravity += 1
        if self.y > MAX_HEIGHT-self.height : 
            self.y = MAX_HEIGHT-self.height


        for platform in self.platformGroup : 
            if platform.rect.colliderect(self.rect) :
                self.isOnPlatform = True
                
                #check if above platform
                if self.rect.bottom < platform.rect.centery :

                    if self.vel >= 0 :
                        self.jumpCount = 8
                        if not(self.isJump) :
                            self.y = platform.rect.centery - self.height - 8
                        self.isJump = False
                        self.isOnPlatform = True
            else :
                self.isOnPlatform = False
                        
    def drawPlayer(self, window) :
        window.blit(self.player , (self.x , self.y))
        self.rect.update(self.x, self.y, self.width, self.height)
