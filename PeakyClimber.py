import pygame
import sys
from player import Player
from platformClass import Platform
import random
from consts import *

class Game:

    def drawGameWindow(self, window, backGroundImage):
        window.blit(backGroundImage, (0, 0))

    def main(self):

        clock = pygame.time.Clock()
        pygame.init()
        window = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
        pygame.display.set_caption("Peaky Climber")

        platform_group = pygame.sprite.Group()
        p_y = MAX_HEIGHT
        for p in range(5):
            p_w = random.randint(150,200)
            p_x = random.randint(10, MAX_WIDTH - p_w - 10)
            # p_y = 2.2 * (p - 1) * 85 
            p_y -= 120

            platform = Platform(p_x, p_y, p_w)
            platform_group.add(platform)

        isPlaying = True
        backGroundImage = pygame.image.load("./assets/bg2.png")
        player = Player(MAX_WIDTH/2, MAX_HEIGHT - PLAYER_HEIGHT , PLAYER_WIDTH, PLAYER_HEIGHT, 8, platform_group)


        while isPlaying:

            clock.tick(40)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isPlaying = False
            self.drawGameWindow(window, backGroundImage)
            # platform_group.draw(window)

            keys = pygame.key.get_pressed()
            platform_group.draw(window)
            player.movement(keys , 640)
            player.drawPlayer(window)
            pygame.display.update()



PeakyClimber = Game()
PeakyClimber.main()
pygame.quit()
sys.exit()