### LIFESIM v1.0
### This version actually does not change according to the last generation,
### but w.r.t. the current state of the grid
### It also initiates in a completely random state
import os
import time
from life import Life

W = 10

grid = []

if grid == []:
    for i in range(W):
        grid.append([])

    for y in range(W):
        for x in range(W):
            grid[y].append(Life(grid, x, y))



def printGrid(grid):
    print("=====================")
    for y in range(W):
        print("|", end='')
        for x in range(W-1):
            print(grid[y][x], end=' ')
        print(grid[y][W-1], end='|\n')
    print("=====================")


clear = lambda: os.system('cls') #on Windows System


if __name__ == '__main__':
    print("LifeSim v1.0")
    its = int(input('Set number of iterations:'))
    time.sleep(1)
    clear()
    print("Generation 0")
    printGrid(grid)
    for i in range(1,its+1):
        for r in grid:
            for e in r:
                e.nextGen()
        time.sleep(1)
        clear()
        print("Generation", i)
        printGrid(grid)
    #input('Press enter to end')
