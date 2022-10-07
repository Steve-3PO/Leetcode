# Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # identify whether the right side of the midpoint is linear increasing, if it is, then the smallest value must be left of the midpoint. Otherwise it will be on the right of the midpoint
        l = 0
        r = len(nums) - 1
        minseen = 5000
        
        while l <= r:
            
            m = (l + r) // 2
            
            minseen = min(nums[m], minseen)
            
            # check if right side is sorted, if it is move right pointer in
            if nums[m] < nums[r]:
                r = m - 1
                
            # if it isnt the move left in
            else:
                l = m + 1
        
        return minseen