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

    def update(self , player, platform_group) :
     
        if player.score > 1 :
            self.rect.y += 5
            # if self.isMovingLeft :
            #     self.rect.x -= 2
            # else :
            #     self.rect.x += 1

            # if self.rect.x > 410 :
            #     self.isMovingLeft = True

            # if self.rect.x < 30 :
            #     self.isMovingLeft = False
            player.y += 5/(len(platform_group))


        if self.rect.top - player.height>= MAX_HEIGHT :
            self.kill()

        
