import pygame

class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, image_path):
        pygame.sprite.Sprite.__init__(self)
        imageLoader = pygame.image.load(image_path)
        self.image = imageLoader
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self , player, platform_group) :
     
        if player.score > 1 :
            player.y += 5/len(platform_group)
            self.rect.y += 5

        if self.rect.top - player.height>= 680 :
            self.kill()

        
