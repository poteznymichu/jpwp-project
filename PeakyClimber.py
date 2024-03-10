import pygame
import sys
from player import Player
from platformClass import Platform
from button import Button
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

        # statyczne platformy
        platform_group = pygame.sprite.Group()
        p_y = MAX_HEIGHT
        for p in range(6):
            p_w = random.randint(150,200)
            p_x = random.randint(10, MAX_WIDTH - p_w - 10)
            p_y -= 120 - p
            if p == 5 :
                p_x = -200

            platform = Platform(p_x, p_y, p_w)
            platform_group.add(platform)


        backGroundImage = pygame.image.load("./assets/bg2.png")
        player = Player(MAX_WIDTH/2, MAX_HEIGHT - PLAYER_HEIGHT , PLAYER_WIDTH, PLAYER_HEIGHT, 8, platform_group)

        start_button_img = pygame.image.load("./assets/start_btn.png")
        button_width, button_height = start_button_img.get_rect().size
        start_button = Button((MAX_WIDTH - button_width) / 2, (MAX_HEIGHT - 3*button_height) / 2, start_button_img, window)

        exit_button_img = pygame.image.load("./assets/exit_btn.png")
        exit_button_width, exit_button_height = exit_button_img.get_rect().size
        exit_button = Button((MAX_WIDTH - exit_button_width) / 2, (MAX_HEIGHT + exit_button_height) / 2, exit_button_img, window)

        font = pygame.font.SysFont(None, 80)
        title_surface = font.render("Peaky Climber", True, (255, 255, 255))
        title_rect = title_surface.get_rect()
        title_rect.center = (window.get_width() // 2, 100)

        isPlaying = True
        isStartMenuOpen = True
        while isPlaying:

            clock.tick(40)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isPlaying = False

            if isStartMenuOpen :
                window.fill((202, 228, 241))
                window.blit(title_surface, title_rect)

                # rysowanie buttonow i sprawdzanie akcji jednoczesnie
                if start_button.draw_button() :
                    isStartMenuOpen = False

                if exit_button.draw_button() :
                    isPlaying = False
                    
            else :
                self.drawGameWindow(window, backGroundImage)
                platform_group.draw(window)
                player.movement(window.get_width())
                player.drawPlayer(window)

            pygame.display.update()


PeakyClimber = Game()
PeakyClimber.main()
pygame.quit()
sys.exit()