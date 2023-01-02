# Rotate Image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # start with 2 pointers for both horizontal and vertical sides, and consider only the outer most ring each time
        l, r = 0, len(matrix) - 1
        

        # move pointers inwards each turn, until they have met
        while l < r:

            # for each position along the ring
            for i in range(r - l):

                # assign top and bottom, equal to r/l as it is a cube
                top, bottom = l, r

                # top left -> temp variable
                placeholder = matrix[top][l + i]

                # bottom left -> top left 
                matrix[top][l + i] = matrix[bottom - i][l]

                # bottom right -> bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # top right -> bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                #top left -> top right
                matrix[top + i][r] = placeholder

            # change pointers for next ring
            l += 1
            r -= 1
