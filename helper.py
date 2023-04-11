from app import *
import random
from block import Block

# Helper Functions
  
# Function used to check collisions between any two entities
def collisionChecker(rect, ball):
    if pygame.Rect.colliderect(rect, ball):
        return True
  
    return False
  
  
# Function used to populate the blocks
def populateBlocks(blockWidth, blockHeight):
    listOfBlocks = []
    for i in range(-7, 7):
        for j in range(-10, 10):
            listOfBlocks.append(Block(WIDTH/2+35*i,
                                HEIGHT/2+35*j,             
                                blockWidth,
                                blockHeight, 
                                WHITE))

    return listOfBlocks
  
  
# Once all the lives are over, this function waits
# until exit or space bar is pressed and does the 
# corresponding action
def gameOver():
    gameOver = True
      
    while gameOver:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True