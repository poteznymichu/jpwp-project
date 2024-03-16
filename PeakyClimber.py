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
            window.blit(backGroundImage, (0, -1 *i * MAX_HEIGHT+ self.scroll))

        self.scroll += 1.5
        if abs(self.scroll) >= MAX_HEIGHT  :
            self.scroll = 0


    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load("./assets/music.mp3")
        pygame.mixer.music.play(-1) 
        pygame.mixer.music.set_volume(0.03)

    def reset_game(self, player, platform_group, Game_State):
        player.score = 0
        player.x = 400
        player.y = 680 - PLAYER_HEIGHT
        platform_group.empty()
        initial_platform = Platform(300, 680, "./assets/platforma6.png")
        platform_group.add(initial_platform)
        self.scroll = 0
        Game_State = "game"
        return Game_State
    
    def show_score(self,x,y,window,player):
        font = pygame.font.Font('./assets/fontt.otf',32)
        score_show = font.render(("Score "+ str(player.score)),True,(255,255,255))
        window.blit(score_show,(x,y))

    def platformGenerator(self, platform_group) :
        if len(platform_group) < 10 :  
            p_width = 200
            p_x = random.randint(30, MAX_WIDTH - p_width - 30)
            previous_platform = platform_group.sprites()[len(platform_group) - 1]
            p_y = previous_platform.rect.y - 160
            platform = Platform(p_x, p_y, "./assets/platforma6.png")
            platform_group.add(platform)

    def main(self):

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Peaky Climber")

        window = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
        clock = pygame.time.Clock()

        platform_group = pygame.sprite.Group()
        initalPlatform = Platform(300, 680, "./assets/platforma6.png")
        platform_group.add(initalPlatform)

        player = Player(window.get_width()/2, 680 - PLAYER_HEIGHT , PLAYER_WIDTH, PLAYER_HEIGHT, 8)

        ############ Images and fonts ############
        backGroundImage = pygame.image.load("./assets/background2.png")
        menuBackgroundImage = pygame.image.load("./assets/tower2.png")
        jumpSound = pygame.mixer.Sound("./assets/jumpSound.mp3")
        platformImage = "./assets/platforma6.png"
        font = pygame.font.Font("./assets/fontt.otf", 56)
        smallFont = pygame.font.Font("./assets/fontt.otf", 32)
        title = "Peaky Climber"
        title_render = font.render(title, True, (255, 255, 255))

        ############ Buttons ############
        start_button_img = pygame.image.load("./assets/start_btn_3.png")
        button_height = start_button_img.get_rect().height
        start_button = Button((20) , (MAX_HEIGHT - 1*button_height) / 2 + 50, start_button_img, window)
        startButtonText = "START"
        startButtonText_renderer = font.render(startButtonText, True, (255, 255, 255))

        exit_button_img = pygame.image.load("./assets/exit_btn_3.png")
        exit_button_height = exit_button_img.get_rect().height
        exit_button = Button((20) , (MAX_HEIGHT + exit_button_height) / 2 + 100, exit_button_img, window)
        exitButtonText = "EXIT"
        exitButtonText_renderer = font.render(exitButtonText, True, (255, 255, 255))

        reset_button = Button((20) , (MAX_HEIGHT - 1*button_height) / 2 + 150, exit_button_img, window)
        resetButtonText = "PLAY \n AGAIN"
        resetButtonText_renderer = smallFont.render(resetButtonText, True, (255, 255, 255))

        ############ Music thread ############
        music_thread = threading.Thread(target=self.play_music)
        music_thread.start()


        ############ Game loop ############
        Game_State = "menu"
        isPlaying = True
        while isPlaying:

            clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isPlaying = False
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_SPACE and not(player.isJumping) and not(player.isFalling) :
                        player.isJumping = True
                        player.jumpSound(jumpSound)

            if Game_State == "menu" :

                window.fill((80, 114, 167))
                window.blit(menuBackgroundImage,(130,75))
                window.blit(title_render, ( 40, 50))

                if start_button.draw_button() :
                    Game_State = "game"
                window.blit(startButtonText_renderer, ((45) , (403) ))

                if exit_button.draw_button() :
                    isPlaying = False
                window.blit(exitButtonText_renderer, ((50) , (MAX_HEIGHT + exit_button_height) / 2 + 112))
                
            elif Game_State == "game" :

                self.platformGenerator(platform_group)
                self.drawGameWindow(window, backGroundImage)
                platform_group.update(player,platform_group)
                player.handlePlatforms(platform_group, window)
                player.movement(window)
                player.drawPlayer(window) 
                self.show_score(240,720,window, player)

                if player.rect.top > MAX_HEIGHT :
                    Game_State = "Dead"

            elif Game_State == "Dead" :

                window.fill((80, 114, 167))
                window.blit(menuBackgroundImage,(130,75))
                window.blit(title_render, ( 40, 50))
                self.show_score(50,430,window,player)

                if reset_button.draw_button() :
                    Game_State = self.reset_game(player, platform_group, Game_State)
                window.blit(resetButtonText_renderer, (65, 500))

            pygame.display.update()


PeakyClimber = Game()
PeakyClimber.main()
pygame.quit()
sys.exit()
