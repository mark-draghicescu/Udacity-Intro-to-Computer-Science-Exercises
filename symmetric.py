# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def symmetric(grid):
    if grid == []:
        return True
    gridSize = len(grid)
    numCols = len(grid[0])
    if not gridSize == numCols:
        return False
    i = 0
    while i <= (gridSize - 1):
        j = 0
        while j <= (gridSize - 1):
            if not (grid[i][j] == grid[j][i]):
                return False
            j = j + 1
        i = i + 1
    return True
