import pygame
from consts import *

class Button :
    def __init__(self,x,y,image,window):
        self.window = window
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw_button(self) :
        self.window.blit(self.image, (self.rect.x , self.rect.y))
        mouse_position = pygame.mouse.get_pos()
        button_action = False

        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0] and not(self.clicked):
                self.clicked = True
                button_action = True

        if not(pygame.mouse.get_pressed()[0]) :
            self.clicked = False
        
        return button_action

            
