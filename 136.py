# Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Initialize the unique number
        uniqNum = 0
        
        # Traverse all elements through the loop
        for num in nums:
            
            # Concept of XOR
            uniqNum ^= num
            
        return uniqNum 