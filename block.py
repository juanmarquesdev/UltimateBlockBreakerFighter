from app import *

class Block:
    def __init__(self, posx, posy, width, height, color):
        """Costructor function to the Block

        Args:
            posx (int): Position on the x-axis
            posy (int): Position on the y-axis
            width (int): Block width
            height (int): Block height
            color (tuple): Block color
        """
        self.posx, self.posy = posx, posy
        self.width, self.height = width, height
        self.color = color
        self.damage = 100

        # The white blocks have the health of 200. 
        # So, the ball must hit it twice to break
        if color == WHITE:
            self.health = 200
        else:
            self.health = 100

        # The rect variable is used to handle the placement 
        # and the collisions of the object
        self.block_rect = pygame.Rect(
            self.posx, self.posy, self.width, self.height)
        self.block = pygame.draw.rect(screen, 
                                self.color, self.block_rect)
        
    # Used to render the object on the screen if and 
    # only if its health is greater than 0
    def display(self):
        if self.health > 0:
            self.brick = pygame.draw.rect(screen,
                            self.color, self.block_rect)
            
    # Used to decrease the health of the block and set the Gray color
    def hit(self):
        self.health -= self.damage
        self.color = GRAY

    # Used to get the rect of the object
    def get_rect(self):
        return self.block_rect

    # Used to get the health of the object
    def get_health(self):
        return self.health