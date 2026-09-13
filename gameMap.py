NONE = 0
BLACK = 1
WHITE = 2

class Point:
    def __init__(self):
        self.color:int = NONE
    
    def place(self, color:int):
        self.color:int = color

class Map:
    def __init__(self):
        self.WIDTH = 15
        self.HEIGHT = 15
        self.map:list[list[Point]] = []
        for j in range(self.HEIGHT):
            self.map.append([])
            for i in range(self.WIDTH):
                self.map[j].append(Point())