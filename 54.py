# Spiral Matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # result array to append values to
        res = []

        # initialise pointers for all sides, after each rotation they should all approach the middle
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)

        # keep going until points have crossed
        while (left < right) and (top < bottom):

            # from top left to top right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # from top right to bottom right
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # check condition half way
            if not (left < right and top < bottom):
                break

            # from bottom right to bottom left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # from bottom left to top left
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res