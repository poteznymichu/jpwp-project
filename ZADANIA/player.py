import pygame
from consts import *
class Player:

    def __init__(self, x, y, width, height, velocity):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.velocity = velocity
        self.player = pygame.image.load("./player/player.png").convert_alpha()
        self.rect = self.player.get_rect()
        self.isOnPlatform = True
        self.isJumping = False
        self.jumpCount = 8
        self.score = 0
        self.isFalling = False
        self.isLeft = False
        self.isRight = False
        self.HP = 3
        self.canDieRotate = False


    def movement(self, window):

        if self.isJumping  :
                if self.jumpCount >= -8 :
                    self.y -= (self.jumpCount * abs(self.jumpCount)) * 1
                    self.jumpCount -= 1
                    if self.jumpCount < 0:
                        if self.isLeft:
                            self.player = pygame.image.load("./player/jumpDownl.png").convert_alpha()
                        else:
                            self.player = pygame.image.load("./player/jumpDownr.png").convert_alpha()
                    else: 
                        if self.isLeft:
                            self.player = pygame.image.load("./player/jumpUpl.png").convert_alpha()
                        else:
                            self.player = pygame.image.load("./player/jumpUpr.png").convert_alpha()
                else:
                    self.jumpCount = 8  
                    self.isJumping = False
        else:
            self.player = pygame.image.load("./player/player.png").convert_alpha()


        if self.score > 1 and self.score < 30 :
            self.y += 4
        elif self.score >= 30 and self.score < 60 :
            self.y += 5
        elif self.score >= 60 and self.score < 100 :
            self.y += 6
        elif self.score >= 100 :
            self.y += 7


        #Zadanie 2
        #Stworz obiekt keys, ktory sprawdza jaki przycisk jest wcisniety
        #Potem odkomentuj czesc kodu odpowiedzialna za poruszanie playera

        '''

            #Miejsce na kod

        '''

        # if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.x > self.velocity:
        #     self.player = pygame.image.load("./player/l1.png").convert_alpha()
        #     self.isLeft = True
        #     self.isRight = False
        #     self.x -= self.velocity

        # if (keys[pygame.K_d] or keys[pygame.K_RIGHT])  and self.x < window.get_width() - self.width - self.velocity :
        #     self.player = pygame.image.load("./player/r1.png").convert_alpha()
        #     self.isRight = True
        #     self.isLeft = False
        #     self.x += self.velocity

        # if not self.isOnPlatform and not self.isJumping :
        #     self.y += self.velocity * 2
        #     self.isFalling = True
        # else:
        #     self.isFalling = False 

                

    def handlePlatforms(self,platform_group, window):
        platform_group.draw(window)

        if self.isFalling :
            if self.isLeft:
                self.player = pygame.image.load("./player/jumpDownl.png").convert_alpha()
            else:
                self.player = pygame.image.load("./player/jumpDownr.png").convert_alpha()
            for platform in platform_group : 
                if self.rect.colliderect(platform.rect) :
                    if round(self.rect.centery)  < round(platform.rect.top) :
                            
                            self.jumpCount = 8
                            self.isJumping = False
                            if not self.isJumping :
                                self.y = platform.rect.top - self.height 
                                self.isOnPlatform = True
                                self.score+=1
                else :
                    self.isOnPlatform = False
        else : 
            for platform in platform_group : 
                if self.rect.colliderect(platform.rect) :
                    if round(self.rect.centery)  < round(platform.rect.top) and self.jumpCount <= 0 :
                            
                            self.jumpCount = 8
                            self.isJumping = False
                            if not self.isJumping :
                                self.y = platform.rect.top - self.height 
                                self.isOnPlatform = True
                                self.score+=1
                else :
                    self.isOnPlatform = False

        for platform in platform_group : 
            if round(self.y) == round(platform.rect.top) - self.height and round(self.rect.right) >= round(platform.rect.left) and round(self.rect.left) <= round(platform.rect.right):
                self.isOnPlatform = True
                self.y = platform.rect.top - self.height

    def drawPlayer(self, window) :


        #Zadanie 2
        #Uzupełnij kod o funckje rysującą playera
        '''

            #Miejsce na kod 

        '''    

        self.rect.y = self.y
        self.rect.x = self.x