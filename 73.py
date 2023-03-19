# Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # we will use top row of index to mark as whether the columns should be zeroed 
        # and we will use the left column to tell us whether the rows should be zeroed
        # we require one extra slot for the [0][0] as it is part of both
        # chosen to have [0][0] used to determine if the column is zeroed with an extra variable to use dfor the row
        topleft = False

        # iterating through each value
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                # when we find a zero
                if matrix[i][j] == 0:

                    # set the top of the column to zero to indicate that whole column must be zeroed
                    matrix[0][j] = 0

                    # check if we are in the first row
                    if i > 0:

                        # if not we set the first index of the row to zero to indicate that whole row must be zeroed
                        matrix[i][0] = 0
                    else: 

                        # if we are at the top row we must use the extra variable to tell us the row should be zeroed
                        topleft = True

        # ignoring the first row and column we can fill out all other spaces quickly 
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if (matrix[0][j] == 0) or (matrix[i][0] == 0):
                    matrix[i][j] = 0

        # for the first column, if origin is zero we can fill in the rest
        if matrix[0][0] == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
            
        # for the first row we must use our extra variable, if True we know we must set all values to zero
        if topleft == True:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
                    
        return matrix