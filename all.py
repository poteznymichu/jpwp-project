import pygame
import sys
from player import Player
from platformClass import Platform


class Game:

    def drawGameWindow(self, window, backGroundImage, platform):
        window.blit(backGroundImage, (0, 0))
        scaled_image = pygame.transform.scale(platform.image, (platform.length_width, 170))
        window.blit(scaled_image, (platform.random_x, platform.random_y))
        pygame.display.update()

    def main(self):
        MAX_WIDTH = 640
        MAX_HEIGHT = 680
        PLAYER_WIDTH = 67
        PLAYER_HEIGHT = 64
        clock = pygame.time.Clock()
        player = Player(MAX_WIDTH//2, MAX_HEIGHT-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, 8)
        pygame.init()
        window = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
        pygame.display.set_caption("Jumpinho")
        isPlaying = True
        backGroundImage = pygame.image.load("./assets/bg2.png")
        platform = Platform(player, MAX_WIDTH, MAX_HEIGHT)

        while isPlaying:

            clock.tick(40)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isPlaying = False
            self.drawGameWindow(window, backGroundImage, platform)

            keys = pygame.key.get_pressed()
            player.movement(keys , 640)
            player.update_jump(platform)
            player.drawPlayer(window)





Jumpinho = Game()
Jumpinho.main()
pygame.quit()
sys.exit()