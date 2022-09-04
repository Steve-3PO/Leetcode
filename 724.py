# Find Pivot Index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # running sum and a total to change each for loop
        leftSum, rightSum = 0, sum(nums)
        
        # iterate through nums
        for i, val in enumerate(nums):
            
            # subtract current value from total
            rightSum -= val
            
            # is left sum equal to right sum return index
            if leftSum == rightSum:
                
                return i
            
            # otherwise add it to the left sum
            leftSum += val
            
        return False