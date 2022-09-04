# Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        # require a sum and a new array
        s, c = 0, []
        
        # for each item, add to the sum and append new value
        for i in nums:
            s += i
            c.append(s)
            
        return c