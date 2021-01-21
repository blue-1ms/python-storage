import random
import pygame
import sys
from pygame.locals import *

Snakespeed = 15
Window_Width = 800
Window_Height = 500
Cell_Size = 20

assert Window_Width % Cell_Size == 0, "Window width must be a multiple of cell size."
assert Window_Height % Cell_Size == 0, "Window height must be a multiple of cell size."
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
    pygame.display.set_caption('snake.py')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def runGame():
    startx = random.randint(5, Cell_W - 6)
    starty = random.randint(5, Cell_H - 6)
    wordCoords = [{'x': startx, 'y': starty},
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

    
    if wordCoords[HEAD] ['x'] == -1 or wordCoords[HEAD]['x'] == Cell_W or wordCoords[HEAD]['y'] == -1 or wordCoords[HEAD]['y'] == Cell_H:
        return
    for wormBody in wordCoords[1:]:
        if wormBody['x'] == wordCoords[HEAD]['x'] and wormBody['y'] == wordCoords[HEAD]['y']:
            return
            
    if wordCoords[HEAD]['x'] == apple['x'] and wordCoords[HEAD]['y'] == apple['y']:
        apple = getRandomLocation()
    else:
        del wordCoords[-1]


    if direction == UP:
        newHead = {'x': wordCoords[HEAD]['x'],
                   'y': wordCoords[HEAD]['y'] - 1}    
    elif direction == DOWN:
        newHead = {'x': wordCoords[HEAD]['x'],
                   'y': wordCoords[HEAD]['y'] + 1}  
    elif direction == LEFT:
        newHead = {'x': wordCoords[HEAD]['x'] - 1,
                   'y': wordCoords[HEAD]['y']}  
    elif direction == RIGHT:
        newHead = {'x': wordCoords[HEAD]['x'] + 1,
                   'y': wordCoords[HEAD]['y']}
    wordCoords.insert(0, newHead)
    DISPLAYSURF.fill(BGColor)
    drawGrid()
    drawWorm(wordCoords)
    drawApple(apple)
    drawScore(len(wordCoords) -3)
    pygame.display.update()
    SnakespeedCLOCK.tick(Snakespeed)

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press any key to play!', True, Blue)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (Window_Width - 200, Window_Height - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('snake.py', True, Blue, Green)
    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(BGColor)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (Window_Width / 2, Window_Height / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get()
            return
        pygame.display.update()
        SnakespeedCLOCK.tick(Snakespeed)
        degrees1 +=3
        degrees2 +=3


def terminate():
    pygame.quit()
    sys.exit()


def getRandomLocation():
    return {'x': random.randint(0, Cell_W - 1), 'y': random.randint(0, Cell_H -1)}


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
    gameSurf = gameOverFont.render('GAME OVER!', True, Red)
    gameRect = gameRect.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (Window_Width / 2, 10)
    overRect.midtop = (Window_Width / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress

    while True:
        if checkForKeyPress():
            pygame.event.get()
            return


def drawScore(score):
    scoreSurf = BASICFONT.render('SCORE: %s' % (score), True, Yellow)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (Window_Width - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawWorm(wordCoords):
    for coord in wordCoords:
        x = coord['x'] * Cell_Size
        y = coord['y'] * Cell_Size
        wormSegmentRect = pygame.Rect(x, y, Cell_Size, Cell_Size)
        pygame.draw.rect(DISPLAYSURF, DGreen, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(
            x + 4, y + 4, Cell_Size - 8, Cell_Size - 8)                                             
        pygame.draw.rect(DISPLAYSURF, Green, wormInnerSegmentRect)


def drawApple(coord):
    x = coord['x'] * Cell_Size
    y = coord['y'] * Cell_Size
    appleRect = pygame.Rect(x, y, Cell_Size, Cell_Size)
    pygame.draw.rect(DISPLAYSURF, Red, appleRect)


def drawGrid():
    for x in range(0, Window_Width, Cell_Size):
        pygame.draw.line(DISPLAYSURF, DGray, (x, 0), (x, Window_Height))
    for y in range(0, Window_Height, Cell_Size):
        pygame.draw.line(DISPLAYSURF, DGray, (0,y), (Window_Width, y))


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
