### LIFE class for lifesim v1.0
import random

STATES = [" ", "■"]

class Life:
    
    def __init__(self, grid, x, y, rand=True, state=None):
        self.state = random.choice([0,1,1,1]) if rand else state
        self.grid = grid
        self.x = x
        self.y = y

    def __str__(self):
        return STATES[self.state]

    def getNBids(self):
        w = len(self.grid[0])
        h = len(self.grid)
        x = self.x
        y = self.y
        temp = [(x-1, y-1),
            (x,y-1), 
            (x+1,y-1), 
            (x-1,y), 
            (x+1,y), 
            (x-1,y+1), 
            (x,y+1), 
            (x+1,y+1), 
                ]
        nbs = []
        for x,y in temp:
            if(x >= 0 and x < w):
                if(y >= 0 and y < h):
                    nbs.append((x,y))
        return nbs
    
    def getLiveNBS(self):
        nbs = self.getNBids()
        total = 0
        for x, y in nbs:
            total += 1 if self.grid[y][x].isAlive() else 0
        return total

    def isAlive(self):
        return self.state != 0

    def nextGen(self):
        nbsAlive = self.getLiveNBS()
        if(self.isAlive and (nbsAlive > 3 or nbsAlive < 2)):
            self.state = 0
        elif(not self.isAlive and nbsAlive == 3):
            self.state = 1
        
    

    
    
