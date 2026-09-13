import gameMap

map = gameMap.Map()
count = 0
running = True
win = gameMap.NONE

DERECTIONS = [
    (0, 1),
    (1, 0),
    (1, 1),
    (1, -1)
]

def acceptPiece(row:int, col:int):
    global count,win,running
    if row >= 0 and col >= 0:
        if map.map[row][col].color == gameMap.NONE and win == gameMap.NONE:
            if count % 2 == 0:
                map.map[row][col].place(gameMap.BLACK)
            else:
                map.map[row][col].place(gameMap.WHITE)

            count += 1

    result = checkWin(row, col)
    if result != gameMap.NONE:
        win = result
        if win == gameMap.BLACK:
            print("黑方获胜")
        else:
            print("白方获胜")
    elif count >= 225:
        win = -1
        print("平局")
    
    print(count)

def checkWin(row:int, col:int) -> int:
    color = map.map[row][col].color

    if color == gameMap.NONE:
        return gameMap.NONE
    
    for dr, dc in DERECTIONS:
        total = 1
        
        r, c = row + dr, col + dc
        while (0 <= r < 15 and 0 <= c < 15) and (map.map[r][c].color == color):
            total += 1
            r += dr
            c += dc

        r, c = row - dr, col - dc
        while (0 <= r < 15 and 0 <= c <15) and (map.map[r][c].color == color):
            total += 1
            r -= dr
            c -= dc

        if total >= 5:
            return color
        
    return gameMap.NONE


