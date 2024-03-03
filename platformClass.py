import pygame
import random


class Platform:

    def __init__(self,player,MAX_WIDTH,MAX_HEIGHT) -> None:
        BASE = 70
        self.MAX_WIDTH = MAX_WIDTH
        self.MAX_HEIGHT = MAX_HEIGHT
        self.player = player
        self.space_available = self.MAX_WIDTH//2
        self.length_width = random.randint(player.width*2+10, self.space_available)
        self.random_x = random.randint(15,self.MAX_WIDTH-self.length_width)
        self.random_y = self.player.y - BASE - self.player.height + 15
        self.image = pygame.image.load('./assets/platform3.png')