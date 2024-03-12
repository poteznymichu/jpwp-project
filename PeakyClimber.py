import os
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


    def handlePlayerScore(self, player, platformGroup, visitedPlatforms) :

        for platform in platformGroup :
            if player.y == platform.rect.top - player.height :
                if platform.rect.top not in visitedPlatforms :
                    player.score += 1
                    visitedPlatforms.append(platform.rect.top) 
                    print(f"Player Score : {player.score}")
    

    def generatePlatforms(self,platformGroup,quantity):
        
        p_y = MAX_HEIGHT
        for p in range(quantity):

            p_width = 200
            p_x = random.randint(30, MAX_WIDTH - p_width - 30)
            p_y -= 130 - p

            platform = Platform(p_x, p_y, "./assets/platform3.png")
            platformGroup.add(platform)

    def main(self):

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Peaky Climber")
        window = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
        backGroundImage = pygame.image.load("./assets/bg2.png")
      
        platform_group = pygame.sprite.Group()
        self.generatePlatforms(platform_group,4)

        player = Player(window.get_width()/2, window.get_height() - PLAYER_HEIGHT , PLAYER_WIDTH, PLAYER_HEIGHT, 8)

        start_button_img = pygame.image.load("./assets/start_btn.png")
        button_width, button_height = start_button_img.get_rect().size
        start_button = Button((MAX_WIDTH - button_width) / 2, (MAX_HEIGHT - 3*button_height) / 2, start_button_img, window)

        exit_button_img = pygame.image.load("./assets/exit_btn.png")
        exit_button_width, exit_button_height = exit_button_img.get_rect().size
        exit_button = Button((MAX_WIDTH - exit_button_width) / 2, (MAX_HEIGHT + exit_button_height) / 2, exit_button_img, window)

        isPlaying = True
        clock = pygame.time.Clock()
        menuBackgroundImage = pygame.image.load("./assets/menuBackground.png")
        jumpSound = pygame.mixer.Sound("./assets/jumpSound.mp3")

        Game_State = "menu"
        visitedPlatforms = []

        while isPlaying:

            clock.tick(40)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isPlaying = False
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_SPACE and not(player.isJumping) :
                        player.isJumping = True
                        player.jumpSound(jumpSound)

            if Game_State == "menu" :

                window.blit(menuBackgroundImage,(0,0))

                if start_button.draw_button() :
                    Game_State = "game"

                if exit_button.draw_button() :
                    isPlaying = False
                    
            elif Game_State == "game" :
                self.drawGameWindow(window, backGroundImage)
                self.handlePlayerScore(player, platform_group, visitedPlatforms)
                player.movement(window)
                player.handlePlatforms(platform_group, window)
                player.handleGravity(3.5)
                player.drawPlayer(window) 
                

            pygame.display.update()


PeakyClimber = Game()
PeakyClimber.main()
pygame.quit()
sys.exit()
