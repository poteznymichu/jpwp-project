import pygame
from consts import *

class Button :
    def __init__(self,x,y,image,window):
        self.window = window
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.hovered = False
        self.last_hovered_state = False

    def draw_button(self) :
        self.window.blit(self.image, (self.rect.x , self.rect.y))
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        if self.rect.collidepoint(mouse_pos) or (self.hovered and not self.rect.collidepoint(mouse_pos)):
            self.hovered = self.rect.collidepoint(mouse_pos) #przypisze true do hovered jak bedzie w tym prostokacie jak to spelnione self.rect.collidepoint(mouse_pos): da true
        else:
            self.hovered = False

        #tu zeby sprawdzalo tylko jak sie stan zmienil bo tak to sie zmienial naprzemiennie
        if self.hovered != self.last_hovered_state:
            if self.hovered:
                pygame.mouse.set_cursor(pygame.cursors.arrow)
            else:
                pygame.mouse.set_cursor()
            self.last_hovered_state = self.hovered

        button_action = False
        #idk czy to dobry approach wywalem zmienna clicked bo i tak raz bedzie klikane, wszedzie zakladalem ze tylko raz sie uzyje menu
        if self.hovered and mouse_click:
            pygame.mouse.set_cursor()
            button_action = True
        elif not mouse_click:
            button_action = False

        return button_action
