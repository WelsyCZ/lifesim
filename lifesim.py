#### Lifesim v2.0
import time
import copy
import os

W = None

# blinker
blinker = [ [0,0,0,0,0],
            [0,0,0,0,0],
            [0,1,1,1,0],
            [0,0,0,0,0],
            [0,0,0,0,0] ]

blinkers = [ [0,0,0,0,0,0],
            [0,1,1,1,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,1,1,1,0],
            [0,0,0,0,0,0] ]

toad = [[0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,1,1,1,0],
        [0,1,1,1,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
]

glider = [[0,1,0,0,0,0,0],
          [0,0,1,0,0,0,0],
          [1,1,1,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0]
]

beacon = [[0,0,0,0,0,0],
          [0,1,1,0,0,0],
          [0,1,1,0,0,0],
          [0,0,0,1,1,0],
          [0,0,0,1,1,0],
          [0,0,0,0,0,0],
]

presets = [blinker, blinkers, toad, glider, beacon]

def printGrid(grid):
    delimiter = ["=" for i in range(2*W + 1)]
    delimiter = ''.join(delimiter)
    print(delimiter) 
    for y in range(W):
        print("|", end='')
        for x in range(W-1):
            print("■" if grid[y][x] == 1 else " ", end=' ')
        print("■" if grid[y][W-1] == 1 else " ", end='|\n')
    print(delimiter)


def getNBids(grid, x, y):
    w = len(grid[0])
    h = len(grid)
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

def countLivingNBS(grid, pointx, pointy):
    ids = getNBids(grid, pointx, pointy)
    total = 0
    for x, y in ids:
        total += grid[y][x]
    return total


def nextGen(grid, backup=True):
    if(backup):
        ret = copy.deepcopy(grid)
    else:
        ret = grid
    for y in range(W):
        for x in range(W):
            count = countLivingNBS(grid, x, y)
            if(grid[y][x] == 1 and (count < 2 or count > 3)):
                ret[y][x] = 0
            elif(grid[y][x] == 0 and count == 3):
                ret[y][x] = 1
            else:
                ret[y][x] = grid[y][x]
    return ret

clear = lambda: os.system("cls")

if __name__ == "__main__":
    backup = True
    clear()
    print("Lifesim v2.0")
    msg = "Choose a preset - blinker(0), blinkers(1), toad(2), glider(3),\nbeacon(4): "
    grid = presets[int(input(msg))]
    W = len(grid)
    printGrid(grid)
    iters = int(input("How many iterations: "))
    time.sleep(0.25)
    print("OK")
    time.sleep(0.25)
    for i in range(iters+1):
        clear()
        print("Generation", i)
        printGrid(grid)
        grid = nextGen(grid, backup)
        time.sleep(1)
