import pygame
import gameLogic
import gameMap

pygame.init()
FONT = pygame.font.Font("./resources/fonts/msyh.ttc", 60)

WIDTH = 1000
HEIGHT = 1000
BG_COLOR = (222, 194, 156)
LINE_COLOR = (10, 10, 10)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RADIUS = 20

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("五子棋")

#CLOCK = pygame.time.Clock()

def drawMap():
    SCREEN.fill(BG_COLOR)
    for i in range(15):
        pygame.draw.line(SCREEN, LINE_COLOR, (80 + i * 60, 80), (80 + i * 60, HEIGHT - 80))
    for j in range(15):
        pygame.draw.line(SCREEN, LINE_COLOR, (80, 80 + j * 60), (WIDTH - 80, 80 + j * 60))

    for row in range(len(gameLogic.map.map)):
        for col in range(len(gameLogic.map.map[row])):
            drawPiece(row, col)


def drawPiece(row:int, col:int):
    #color = ()
    #print(gameLogic.map.map[row][col].color)
    if gameLogic.map.map[row][col].color == gameMap.WHITE:
        pygame.draw.circle(SCREEN, WHITE, (col * 60 + 80, row * 60 + 80), RADIUS)
    elif gameLogic.map.map[row][col].color == gameMap.BLACK:
        pygame.draw.circle(SCREEN, BLACK, (col * 60 + 80, row * 60 + 80), RADIUS)

    #pygame.draw.circle(SCREEN, (0,0,0), (col * 60 + 80, row * 60 + 80), RADIUS)

def drawText(text:str, pos:tuple[int,int]):
    SCREEN.blit(FONT.render(text, True, LINE_COLOR), pos)

def init():
    drawMap()
    pygame.display.flip()

def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLogic.running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            #drawMap()
            mx, my = event.pos
            if 50 <= mx <= WIDTH - 50 and 50 <= my <= HEIGHT - 50:
                col = (mx - 50) // 60
                row = (my - 50) // 60
                gameLogic.acceptPiece(row, col)
                #drawPiece(row, col)
            else:
                col = -1
                row = -1

            print((mx, my), (row, col))
            drawMap()

            if gameLogic.win != gameMap.NONE:
                if gameLogic.win == -1:
                    text = "平局"
                elif gameLogic.win == gameMap.BLACK:
                    text = "黑方获胜"
                else:
                    text = "白方获胜"
                
                drawText(text, (350, 30))

            #gameLogic.checkLine()

            #gameLogic.acceptPiece(row, col)
            #drawPiece(row, col)

            pygame.display.flip()