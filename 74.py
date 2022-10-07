# Search a 2D Matrix

import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # until 1 row has been select, keep running binary search
        while len(matrix) > 1:
            
            mid = int(ceil((len(matrix) - 1) / 2))
        
            if matrix[mid][0] == target:
                return True
        
            elif matrix[mid][0] > target:
                if (mid - 1) == -1:
                    return False
                matrix = matrix[:mid]
                
            elif matrix[mid][0] < target:
                matrix = matrix[mid:]
                
        # until 1 value is selected, keep running binary search
        while len(matrix[0]) > 1:
            
            m = int(ceil((len(matrix[0]) - 1) / 2))
            
            if matrix[0][m] == target:
                return True
            elif matrix[0][m] < target:
                matrix[0] = matrix[0][m:]
            elif matrix[0][m] > target:
                matrix[0] = matrix[0][:m]
            
        # final check if value is the target
        if matrix[0][0] == target:
            return True
        return False