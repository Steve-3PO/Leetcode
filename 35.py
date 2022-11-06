# Seach Insert Position 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # require 2 pointers
        l = 0
        r = len(nums) - 1
        
        # while pointers have not crossed
        while l <= r:
            
            # calculate a mid value
            mid = (l + r) // 2
            
            # reurn mid if == target
            if nums[mid] == target:       
                return mid
            
            # when all array has been checked return the corresponding index
            elif l == r:            
                if nums[mid] > target:    
                    return mid
                else:                     
                    return mid + 1 
                
            # otherwise adjust the l and r pointers
            elif nums[mid] > target:
                r = mid 
            else:
                l = mid + 1
                
       