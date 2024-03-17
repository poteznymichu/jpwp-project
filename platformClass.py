import pygame
from consts import *

class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, image_path):
        pygame.sprite.Sprite.__init__(self)
        imageLoader = pygame.image.load(image_path)
        self.image = imageLoader
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.isMovingLeft = False
        self.downSpeed = 5
        self.leftSpeed = 4
        self.rightSpeed = 2

    def update(self , player) :

        if player.score >= 30 and player.score < 60 :
            self.downSpeed = 6
        elif player.score >= 60 and player.score < 100 :
            self.downSpeed = 7
        elif player.score >= 100 :
            self.downSpeed  = 8

        if player.score > 1 :
            
            self.rect.y += self.downSpeed

            if self.isMovingLeft :
                self.rect.x -= self.leftSpeed
            else :
                self.rect.x += self.rightSpeed

            if self.rect.x > 410 :
                self.isMovingLeft = True

            if self.rect.x < 30 :
                self.isMovingLeft = False


        if self.rect.top - player.height>= MAX_HEIGHT :
            self.kill()

        
