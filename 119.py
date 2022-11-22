# Pascal's Triangle II

from math import comb

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        # empty array
        arr = []
        
        # for i in range up to row index
        for i in range((rowIndex + 1)):
            
            # append rowindex choose index of position
            arr.append(comb(rowIndex, i))
            
        return arr