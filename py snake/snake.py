import random, pygame, sys
from pygame.locals import *

Snakespeed = 20
Window_Width = 800
Window_Height = 600
Cell_Size = 20

assert Window_Width % Cell_Size == 0
assert Window_Height % Cell_Size == 0
Cell_W = int(Window_Width / Cell_Size)
Cell_H = int(Window_Height / Cell_Size)

White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
DRed = (150, 0, 0)
Green = (0, 255, 0)
DGreen = (0, 155, 0)
DGray = (40, 40, 40)
Yellow = (255, 255, 0)
Blue = (0, 0, 255)
DBlue = (0, 0, 150)

BGColor = Black

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0 


def main():
    global SnakespeedCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    SnakespeedCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((Window_Width, Window_Height))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 15)
    pygame.display.set_caption('Snake')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def runGame():
    startx = random.randint(5, Cell_W - 6)
    starty = random.randint(5, Cell_H - 6)
    Coordinates = [{'x': startx, 'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT


    apple = getRandomLocation()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT) and direction != RIGHT:
                    direction = LEFT
            elif (event.key == K_RIGHT) and direction != LEFT:
                    direction = RIGHT
            elif (event.key == K_UP) and direction != DOWN:
                    direction = UP
            elif (event.key == K_DOWN) and direction != UP:
                    direction = DOWN
            elif event.key == K_ESCAPE:
                terminate()

    
    if Coordinates[HEAD] ['x'] == -1 or Coordinates[HEAD]['x'] == Cell_W or Coordinates[HEAD]['y'] == -1 or Coordinates[HEAD]['y'] == Cell_H:
        return
    for wormBody in Coordinates[1:]:
        if wormBody['x'] == Coordinates[HEAD]['x'] and wormBody['y'] == Coordinates[HEAD]['y']:
            return
            

    
                                                    