import pygame
import math as m
class Player:

    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.isJump = False
        self.jumpCount = 8

    def movement(self, keys, windowWidth):

        if keys[pygame.K_a] or keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]  and self.x < windowWidth - self.width - self.vel:
            self.x += self.vel
        
        if not(self.isJump) and keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            self.isJump = True

    def update_jump(self,platform):
        #print("x: " + str(self.x))
        #print("y: " + str(m.floor(self.y - self.height)))
        #print("latform _ x: " + str(m.floor(platform.random_x)))
        #print("latform _ width: " + str(platform.length_width))
        if self.isJump:
            if self.jumpCount >= -8:
                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5 + self.jumpCount
                self.jumpCount -= 1
            else:
                self.jumpCount = 8  
                self.isJump = False

    def onPlatform(self,platform):
        if (m.floor(self.y - self.height) == m.floor(platform.random_y)-2) and platform.random_x <= self.x-self.width and self.x+self.width <= platform.random_x + platform.length_width:
            return True
        else:
            return False

    def drawPlayer(self, window) :
        player = pygame.image.load("./assets/player.jpg")
        window.blit(player , (self.x , self.y))
        pygame.display.update()