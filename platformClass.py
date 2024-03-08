import pygame

class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        imageLoader = pygame.image.load('./assets/platform3.png')
        self.image = pygame.transform.scale(imageLoader,(width,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y