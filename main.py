import gameGUI
import gameLogic

if __name__ == "__main__":
    gameGUI.init()
    while gameLogic.running:
        gameGUI.update()