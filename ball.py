import pygame
from app import *

class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        """Constructor function for the Ball class

        Args:
            posx (int): Position on the x-axis
            posy (int): Position on the y-axis
            radius (int): Ball radius
            speed (int): Ball speed
            color (tuple): Ball color
        """
        self.starting_x = posx
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        # Setting the direction the ball moves
        self.xFac = 1
        self.yFac = -1
        # Drawing the ball 
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1

    def display(self):
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)
        
    def update(self):
        """Update the position of the ball and returns if a player scores

        Returns:
            int: 1 if the player2 scores, -1 if the player1 scores
        """
        
        self.posx += self.speed*self.xFac
        self.posy += self.speed*self.yFac

        # If the ball hits the top or bottom surfaces,
        # then the sign of yFac is changed and it
        # results in a reflection
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1

        # If the ball touches the left wall for the first time,
        # The firstTime is set to 0 and we return 1
        # indicating that player2 has scored
        # firstTime is set to 0 so that the condition is
        # met only once and we can avoid giving multiple
        # points to the player
        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= WIDTH and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0
        
    # Used to reset the position of the ball
    # to the center of the screen
    def reset(self):
        self.posx = self.starting_x
        self.posy = HEIGHT//2
        self.xFac *= -1
        self.firstTime = 1
  
    # Used to reflect the ball along the X-axis
    def hit(self):
        self.xFac *= -1
  
    def get_rect(self):
        return self.ball