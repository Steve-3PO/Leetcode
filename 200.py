# Number of Islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # remove edge case
        if not grid:
            return 0

        # count of islaands
        islands = 0

        # max size of column and row
        col = len(grid[0])
        row = len(grid)

        # check function that converts island 1's into #'s
        def check(index, column):

            # if values are in bounds and it is a "1", then change to a "#" and continue in each direction
            if (column >= 0 and column < col) and (index >= 0 and index < row) and (grid[index][column] == "1"):
                grid[index][column] = "#"
                check(index + 1, column)
                check(index - 1, column)
                check(index, column + 1)
                check(index, column - 1)
            else:
                return

        # iterate through each row and if a "1" is found, run the check to find the rest of the island and increment the count.
        for y in range(row):
            for x in range(col):
                if grid[y][x] == "1":
                    check(y, x)
                    islands += 1

        return islands
                
                