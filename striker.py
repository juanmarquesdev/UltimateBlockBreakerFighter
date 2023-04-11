import pygame
from app import *

class Striker:
    def __init__(self, posx, posy, width, height, speed, color):
        """Constructor function for the Striker class

        Args:
            posx (integer): X Position
            posy (integer): Y Position
            width (integer): Width of the Striker
            height (integer): Height of the Striker
            speed (integer): Speed of the Striker
            color (tuple): Color of the Striker
        """
        
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        
        # O Controlador lida com a posição e colisão do objeto
        self.controller = pygame.Rect(posx, posy, width, height)
        # Desenha o objeto na tela
        self.drawn = pygame.draw.rect(screen, self.color, self.controller)
        
    def display(self):
        self.drawn = pygame.draw.rect(screen, self.color, self.controller)
        
    def update(self, yFac):
        """
        Used to upfate the state of the object
        
        Args:
            yFac (integer): the direction the object is moving
                yFac == -1 ==> Upwards;
                yFac == 0 ==> Not Moving;
                yFac == 1 ==> Downwards;
        """
        self.posy = self.posy + self.speed * yFac

        if self.posy <= 0:
            self.posy = 0
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - self.height
        
        self.controller = (self.posx, self.posy, self.width, self.height)
        

    def diplay_score(self, text, score, x, y, color):
        text = font20.render(text + str(score), True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)
        
    
    def get_rect(self):
        return self.controller
        