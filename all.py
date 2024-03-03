import pygame
import sys
import random
import math as m


class Player:

    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.isJump = False
        self.jumpCount = 8

    def onPlatform(self,platform):
        if (m.floor(self.y - self.height) == m.floor(platform.random_y)-2) and platform.random_x <= self.x-self.width and self.x+self.width <= platform.random_x + platform.length_width:
            return True
        else:
            return False

    def jump(self):
        if not self.isJump:
            self.isJump = True

    def move(self, direction):
        MAX_WIDTH = 640
        if direction == "LEFT" and self.x - self.vel > 20:
            self.x -= self.vel
        elif direction == "RIGHT" and self.x + self.vel < MAX_WIDTH - 20 - self.width:
            self.x += self.vel


    def update_jump(self,platform):
        #print("x: " + str(self.x))
        #print("y: " + str(m.floor(self.y - self.height)))
        #print("latform _ x: " + str(m.floor(platform.random_x)))
        #print("latform _ width: " + str(platform.length_width))
        if self.isJump:
            if self.jumpCount >= -8:
                self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5 + self.jumpCount
                self.jumpCount -= 1
            else:
                self.jumpCount = 8  
                self.isJump = False



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
        self.image = pygame.image.load('platform3.png')


class Game:
    def draw(self, window, bg, player, platform):
        window.blit(bg, (0, 0))
        scaled_image = pygame.transform.scale(platform.image, (platform.length_width, 170))
        window.blit(scaled_image, (platform.random_x, platform.random_y))
        pygame.draw.rect(window, (255, 0, 0), (player.x, player.y, player.width, player.height))
        pygame.display.update()

    def main(self):
        MAX_WIDTH = 640
        MAX_HEIGHT = 680
        clock = pygame.time.Clock()
        player = Player(MAX_WIDTH//2, MAX_HEIGHT-60, 40, 60, 8)
        pygame.init()
        window = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
        pygame.display.set_caption("First Game")
        run = True
        bg = pygame.image.load("bg2.png")
        platform = Platform(player, MAX_WIDTH, MAX_HEIGHT)

        while run:
            clock.tick(40)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player.move("LEFT")
            if keys[pygame.K_RIGHT]or keys[pygame.K_d]:
                player.move("RIGHT")
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                player.jump()

            player.update_jump(platform)
            self.draw(window, bg, player, platform)

        pygame.quit()
        sys.exit()


main = Game()
main.main()