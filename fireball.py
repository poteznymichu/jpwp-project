import pygame
from consts import *

class fireballClass(pygame.sprite.Sprite) :
    def __init__(self, x,y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load("./assets/fireball1.png").convert_alpha(), (40,70))
        self.rect = pygame.Rect(self.x + 5 , self.y + 10, 30, 50)
        self.damageNoise = pygame.mixer.Sound("./assets/damage.mp3")

    def update(self,window , player) :
        window.blit(self.image, (self.x , self.y))
        self.rect.update(self.x, self.y, 40, 70)
        self.y += self.speed

        if self.rect.colliderect(player.rect) :
            player.HP -= 1
            self.damageNoise.set_volume(0.2)
            self.damageNoise.play()  
            self.y = MAX_HEIGHT 
            self.kill()
        
        if player.HP == 0 :
            self.kill()

        

    