from striker import Striker
from ball import Ball
from app import *
from helper import *

class GameManager:
    def run(self):
        running = True
        
        listOfBlocks = []

        blockWidth, blockHeight = 30, 30

        player1 = Striker(20,0,10,100,10, LIGHT_GREEN)
        player2 = Striker(WIDTH-30, 0, 10, 100, 10, LIGHT_GREEN)
        ball1 = Ball(50, HEIGHT//2, 7, 7, WHITE)
        ball2 = Ball(WIDTH-50, HEIGHT//2, 7, 7, WHITE)
        
        list_of_players = [player1, player2]
        
        player1_score, player2_score = 0, 0
        player1_yFac, player2_yFac = 0, 0

        while running:
            screen.fill(BLACK)

            if not listOfBlocks:
                listOfBlocks = populateBlocks(
                    blockWidth, blockHeight)    

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False    
                    
                elif event.type == pygame.KEYDOWN:
                    # Arrows: player 1
                    if event.key == pygame.K_UP:
                        player1_yFac = -1
                    if event.key == pygame.K_DOWN:
                        player1_yFac = 1

                    #W&S : player 2
                    if event.key == pygame.K_w:
                        player2_yFac = -1
                    if event.key == pygame.K_s:
                        player2_yFac = 1
                
                #Stop the Striker
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player1_yFac = 0
                    elif event.key == pygame.K_w or event.key == pygame.K_s:
                        player2_yFac = 0


            # Collision check
            for block in listOfBlocks:
                if(collisionChecker(block.get_rect(), ball1.get_rect())):
                    ball1.hit()
                    block.hit()
  
                if(collisionChecker(block.get_rect(), ball2.get_rect())):
                    ball2.hit()
                    block.hit()

                if block.get_health() <= 0:
                    listOfBlocks.pop(listOfBlocks.index(block))

            for player in list_of_players:
                if collisionChecker(ball1.get_rect(), player.get_rect()):
                    ball1.hit()
                    
                if collisionChecker(ball2.get_rect(), player.get_rect()):
                    ball2.hit()
                
            player1.update(player1_yFac)
            player2.update(player2_yFac)

            list_of_balls = [ball1,ball2]

            for ball in list_of_balls:
                point = ball.update()

                if point == -1 :
                    player1_score += 1
                elif point == 1:
                    player2_score += 1

                if point:
                    ball.reset()
            
            player1.display()
            player2.display()        
            ball1.display()
            ball2.display()
            
            player1.diplay_score("Player 1: ", player1_score, 100,20,WHITE)
            player2.diplay_score("Player 2: ", player2_score, WIDTH-100,20,WHITE)
            
            for block in listOfBlocks:
                block.display()

            pygame.display.update()
            clock.tick(FPS)
