# Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # aim is to find which side of the midpoint is linearly increasing and check if the target is within that portion, if not move choose the other side of the midpoint
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            
            m = (l + r) // 2
            
            # if target is found at midpoint return m
            if target == nums[m]:
                return m
            
            # check if right is sorted
            elif nums[m] <= nums[r]:
                
                # if right is sorted but target is out of bounds then move right pointer in
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                # else move left in
                else: 
                    l = m + 1
                
            # check if left is sorted
            elif nums[l] <= nums[m]:
                
                # if it is sorted but target is is out of bounds then move left pointer in
                if target < nums[l] or nums[m] < target:
                    l = m + 1
                # otherwise move right in
                else:
                    r = m - 1
                
        return -1
            