from typing import Any
import pygame, sys
import random, time
import numpy as np

def GetMovement(Model, TestSignals: list[np.ndarray], Direction: int,player_speed: int) -> tuple[Any, Any]:
    shift = (len(TestSignals) / 4) * Direction
    rand_picked_num = random.randint(0, 3)
    sample_index = rand_picked_num + shift
    TestSignal = TestSignals[int(sample_index)]
    prediction = Model.predict([TestSignal])
    print("prediction for " + GetClass(int(Direction)), " is  ", GetClass(int(prediction)))
    move = MovementValue(prediction, player_speed)
    return move


def MovementValue(Direction, player_speed) -> tuple[int, int]:
    if Direction == 0:
        return 0, player_speed
    elif Direction == 1:
        return -player_speed, 0
    elif Direction == 2:
        return player_speed, 0
    elif Direction == 3:
        return 0, -player_speed
    else:
        return -1, -1


def GetClass(ClassId: int) -> str:
    Classes = ["Down", "Left", "Right", "Up"]
    return Classes[ClassId]

def CreatWalls(screen_width,screen_height ,wall_size,num_walls,player):
    walls = []
    for i in range(num_walls):
        while True:
            # Generate a new rectangle
            wall = pygame.Rect(random.randint(0, screen_width - wall_size),
                               random.randint(0, screen_height - wall_size),
                               wall_size, wall_size)
            # Check if the new rectangle intersects with any of the existing rectangles
            if not any(wall.colliderect(other_wall) for other_wall in walls) and not wall.colliderect(player):
                # If the new rectangle does not intersect with any of the existing rectangles, add it to the list
                walls.append(wall)
                break
    return walls


def createWinningBall(screen_width, screen_height, wall_size, wall,player):
    while True:
        # Generate a new rectangle for the WinningBall
        WinningBall = pygame.Rect(random.randint(0, screen_width - wall_size),
                                  random.randint(0, screen_height - wall_size),
                                  wall_size, wall_size)
        # Check if the new rectangle intersects with any of the walls or the player
        if not any(WinningBall.colliderect(rect) for rect in wall) and not player.colliderect(WinningBall):
            # If the new rectangle does not intersect with any of the walls or the player, break the loop
            break
    return WinningBall

def DisplayGameItems(screen,wall,player,winning_ball):
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 30, 50), player)
    pygame.draw.rect(screen, (255, 200, 0), winning_ball)
    for rect in wall:
        pygame.draw.rect(screen, (0, 0, 0), rect)
    # Update display
    pygame.display.update()

def Check_win_lose(player,wall,WinningBall):
    if player.colliderect(WinningBall):
        print("Congratulations ,You Win!")
        time.sleep(3)
        pygame.quit()
        sys.exit()
    else:
        # Check for collision with walls
        for rect in wall:
            if player.colliderect(rect):
                print("Game over!")
                time.sleep(3)
                pygame.quit()
                sys.exit()
