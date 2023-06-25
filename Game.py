import Maze
import main, Classification as CL
import pygame, sys
import  time


# Define game settings
screen_width = 800
screen_height = 600
player_size = 30
player_speed = 25
wall_size = 40
num_walls = 25

# load the ML model
Model = CL.LoadModel('SVM')
# load test signals
TestSignels = main.Get_Prepared_Signals(1)
# Initialize Pygame
pygame.init()
# Set up game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Game")

# Create player
player = pygame.Rect(screen_width / 2, screen_height / 2, player_size, player_size)

# Create walls
wall = Maze.CreatWalls(screen_width,screen_height ,wall_size,num_walls,player)
# create Winning ball
WinningBall = Maze.createWinningBall(screen_width, screen_height, wall_size, wall,player)


# Define game loop
while True:
    # time.sleep(.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move player based on input
    keys = pygame.key.get_pressed()
    time.sleep(.05)
    Direction = -1
    if keys[pygame.K_LEFT] and player.left > 0:
        Direction = 1
        # player.move_ip(-player_speed, 0)
    elif keys[pygame.K_RIGHT] and player.right < screen_width:
        Direction = 2
        # player.move_ip(player_speed, 0)
    elif keys[pygame.K_UP] and player.top > 0:
        Direction = 3
        # player.move_ip(0, -player_speed)
    elif keys[pygame.K_DOWN] and player.bottom < screen_height:
        Direction = 0
        # player.move_ip(0, player_speed)
    if Direction != -1:
        Move = Maze.GetMovement(Model, TestSignels, Direction, player_speed)
        player.move_ip(Move[0], Move[1])
    # Draw game objects on screen
    Maze.DisplayGameItems(screen, wall, player, WinningBall)
    # Check for collision with winning rect
    Maze.Check_win_lose(player,wall,WinningBall)

