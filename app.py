import pygame

screen = None
if not screen:
    pygame.init()
    print("Game Initialized")

    # RGB values of standard colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    LIGHT_GREEN = (100, 255, 100)
    GRAY = (128, 128, 128)

    # Setting the font
    font20 = pygame.font.Font('freesansbold.ttf', 20)

    # Creating the screen
    WIDTH, HEIGHT = 900, 600

    screen = pygame.display.set_mode((WIDTH, HEIGHT))   
    
    # Setting the caption
    pygame.display.set_caption("Ultimate BlockBreaker Fighter")

    # Adjust the frame rate
    clock = pygame.time.Clock()
    FPS = 30








