import pygame
import sys
from player import Player
from platformClass import Platform
import random
from consts import *
import threading
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("./player/player.png")


class Game:

    def __init__(self) :
        self.scroll = 0
        self.canSpawnFireball = False

    def drawGameWindow(self, window, backGroundImage):

        #ZADANIE 1
        #Umieść kod, który spowoduje ustawienie tła
        '''
        
            #Miejsce na kod

        '''

        #ZADANIE 2
        #Zmodyfikuj kod z zadania 1 i spowoduj, aby tło było ruchome
        #Koordynaty do funckji blit(2 argument): 0, -1 *i * MAX_HEIGHT+ self.scroll
        #Użyj zmiennej self.scroll, dodatkow dodaj warunek kiedy scroll osiągnie MAX_HEIGHT, żeby tło wróciło na początkową pozycje
        '''
        
            #Miejsce na kod

        '''

     
    def show_score(self,x,y,window,player):
        font = pygame.font.Font('./assets/fontt.otf',32)
        score_show = font.render(("Score "+ str(player.score)),True,(255,255,255))
        window.blit(score_show,(x,y))


    def platformGenerator(self, platform_group) :


        #Zadanie 1
        # Wiedząc że grupa spritów znajduje się pod zmienną platform_group, dodaj pojedyńczą platformę do grupy spriteów
        # Tą samą czynność musisz wykonać w funckji main, po wszystkim możesz odkomentować cały kod funckji platformGenerator

        platform_count = 1
        if len(platform_group) < platform_count:  
            p_width = 200
            p_x = random.randint(30, MAX_WIDTH - p_width - 30)
            #previous_platform = platform_group.sprites()[len(platform_group) - 1]
            #p_y = previous_platform.rect.y - 160
            #platform_sprite = "./assets/platforma6.png"
            #platform = Platform(p_x, p_y, platform_sprite)

        #Zadanie 3
        #Przeanalizuj kod metody i spowoduj zwiększenie liczby wyświetlanych platform 

        #W tej samej funkcji poniżej linii zawierającej platform_sprite doda warunki tak aby zmieniać wygląd platformy
        #Skorzystaj z gotowych zdjec: platform2.png, platform3.png. Wykorzystaj zmienną score

    def main(self):

        pygame.init()
        pygame.mixer.init()

        #Zadanie 1
        #Dodaj tytuł do okna gry
        '''

            #Miejsce na kod

        '''
        pygame.display.set_icon(pygame.image.load("./player/player.png"))
        window = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
        clock = pygame.time.Clock()
        platform_group = pygame.sprite.Group()
        # initalPlatform = Platform(300, 680, "ZADANIA/assets/platform1.png")

        #Zadanie 1
        #Grupa spriteów
        '''

            #Miejsce na kod
        
        '''




        player = Player(window.get_width()/2, 680 - PLAYER_HEIGHT , PLAYER_WIDTH, PLAYER_HEIGHT, 8)

        ############ Images and fonts ############


        backGroundImage = pygame.image.load("./assets/background2.png").convert_alpha()
        background_images = {
        "low": pygame.image.load("./assets/background2.png").convert_alpha(),
        "medium": pygame.image.load("./assets/background3.png").convert_alpha(),
        "high": pygame.image.load("./assets/background4.png").convert_alpha()
    }




        ############ Game loop ############
        isPlaying = True


        while isPlaying:

            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isPlaying = False
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_SPACE and not(player.isJumping) and not(player.isFalling) :
                        player.isJumping = True



            self.platformGenerator(platform_group)
            self.drawGameWindow(window,  backGroundImage )

            platform_group.update(player)
            player.handlePlatforms(platform_group, window)

            if player.HP > 0 :
                player.movement(window)

            player.drawPlayer(window) 


            self.show_score(240,730,window, player)

            if player.rect.top > MAX_HEIGHT :
                break


            pygame.display.update()


PeakyClimber = Game()
PeakyClimber.main()
pygame.quit()
sys.exit()
