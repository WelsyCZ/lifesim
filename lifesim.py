from life import Life

W = 10

grid = []

if grid == []:
    for i in range(W):
        grid.append([])

    for y in range(W):
        for x in range(W):
            grid[y].append(Life(grid, x, y, random=False, state=1 if x==2 or y==2 else 0))



def printGrid(grid):
    print("=====================")
    for y in range(W):
        print("|", end='')
        for x in range(W-1):
            print(grid[y][x], end=' ')
        print(grid[y][W-1], end='|\n')
    print("=====================")




if __name__ == '__main__':
    print("LifeSim v1.0")
    #input('Press enter to start')
    printGrid(grid)
    #input('Press enter to end')
