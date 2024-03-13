import os
import pygame
import sys
from player import Player
from platformClass import Platform
from button import Button
import random
from consts import *
import threading



class Game:
    def __init__(self) :
        self.scroll = 0

    def drawGameWindow(self, window, backGroundImage):
        for i in range(0,2) :
            window.blit(backGroundImage, (0, -1 *i * MAX_HEIGHT + self.scroll))

        self.scroll += 1.5

        if abs(self.scroll) > MAX_HEIGHT :
            self.scroll = 0

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("./assets/music.mp3")
        pygame.mixer.music.play(-1) 
        pygame.mixer.music.set_volume(0.03)
    

    def main(self):

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Peaky Climber")

        window = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
        backGroundImage = pygame.image.load("./assets/bg2.png")
      
        platform_group = pygame.sprite.Group()
        initalPlatform = Platform(300, 600, "./assets/platform3.png")
        platform_group.add(initalPlatform)
        # self.generatePlatforms(platform_group,25)

        player = Player(window.get_width()/2, 600 - PLAYER_HEIGHT , PLAYER_WIDTH, PLAYER_HEIGHT, 8)

        start_button_img = pygame.image.load("./assets/start_btn.png")
        button_width, button_height = start_button_img.get_rect().size
        start_button = Button((MAX_WIDTH - button_width) / 2, (MAX_HEIGHT - 3*button_height) / 2, start_button_img, window)

        exit_button_img = pygame.image.load("./assets/exit_btn.png")
        exit_button_width, exit_button_height = exit_button_img.get_rect().size
        exit_button = Button((MAX_WIDTH - exit_button_width) / 2, (MAX_HEIGHT + exit_button_height) / 2, exit_button_img, window)

        clock = pygame.time.Clock()
        menuBackgroundImage = pygame.image.load("./assets/menuBackground.png")
        jumpSound = pygame.mixer.Sound("./assets/jumpSound.mp3")


        Game_State = "menu"
        isPlaying = True
        visitedPlatforms = []

        music_thread = threading.Thread(target=self.play_music)
        # music_thread.start()


        p_y = 470
        while isPlaying:

            # print(player.isOnPlatform)
            clock.tick(45)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isPlaying = False
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_SPACE and not(player.isJumping) :
                        player.isJumping = True
                        player.jumpSound(jumpSound)

            if Game_State == "menu" :

                if music_thread.is_alive():
                    pygame.mixer.music.stop()
                window.blit(menuBackgroundImage,(0,0))

                if start_button.draw_button() :
                    if not music_thread.is_alive():
                        music_thread.start()
                    Game_State = "game"
                if exit_button.draw_button() :
                    isPlaying = False
                    
            elif Game_State == "game" :

                if len(platform_group) < 10 :  
                    p_width = 200
                    p_x = random.randint(30, MAX_WIDTH - p_width - 30)
                    second_platform = platform_group.sprites()[len(platform_group) - 1]
                    p_y = second_platform.rect.y - 160
                    platform = Platform(p_x, p_y, "./assets/platform3.png")
                    platform_group.add(platform)

                self.drawGameWindow(window, backGroundImage)
                platform_group.update(player,platform_group)
                player.movement(window)
                player.handlePlatforms(platform_group, window)
                player.handleGravity(3.5)
                player.setScore(platform_group, visitedPlatforms)
                player.drawPlayer(window) 

                if player.rect.top> MAX_HEIGHT :
                    Game_State = "Dead"

            elif Game_State == "Dead" :
                window.blit(menuBackgroundImage,(0,0))

            pygame.display.update()


PeakyClimber = Game()
PeakyClimber.main()
pygame.quit()
sys.exit()