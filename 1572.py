# Matrix Diagonal Sum

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        # require a sum value
        sum = 0

        # iterating through each row
        for i in range(len(mat)):

            # add the values of the rows diagonals
            sum += (mat[i][i] + mat[i][-i - 1])

            # if we are in the middle of the matrix we must make sure we only add one value as they will be on the same index
            if i == ((len(mat) - 1) / 2):
                sum -= mat[i][i]
            

        return sum