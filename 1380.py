# Lucky Numbers in a Matrix

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        # we can use an array to track the maximums seen, we can change the corresponding column values everytime we look at a new value
        maxincol = [0] * len(matrix[0])

        # we use a minimums array to track the coords of the minimums in each row
        minimums = []

        # iterating through each row
        for i in range(len(matrix)):

            # initiate a minimum value and its coords
            minseen = matrix[i][0]
            cord1 = i
            cord2 = 0

            # going through each val in a row
            for j in range(len(matrix[0])):

                # update the max seen in the column if it is larger than the current
                maxincol[j] = max(maxincol[j], matrix[i][j])

                # if it is the new minimum in the row, we set the new minimum and keep track of the coords
                if matrix[i][j] < minseen:
                    minseen = matrix[i][j]
                    cord1 = i
                    cord2 = j
                
            # after iterating through the row we will have the location of the minimum in the row
            minimums.append([cord1, cord2])

        # initialise an array which will contain the lucky numbers
        res = []

        # for each coord pair
        for cord1, cord2 in minimums:
            
            # check if it is also the maximum in the col, if it is we append it to the result
            if matrix[cord1][cord2] == maxincol[cord2]:
                res.append(matrix[cord1][cord2])
                
        return res
       



