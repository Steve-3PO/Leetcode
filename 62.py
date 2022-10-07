# Unique Paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # start with a single row of 1s as this will always be the bottom of every array
        row = [1] * n
        
        # continue iterating for each row
        for i in range(m-2, -1, -1):
            
            # start with a new list of 1s
            newrow = [1] * n

            # iterate through every position and add the bottom and right array positions
            for j in range(n-2, -1, -1):
                newrow[j] = newrow[j+1] + row[j]
            
            # change assigment to use the next appended row next iteration
            row = newrow
            
        return row[0]