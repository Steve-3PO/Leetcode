# Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        # need a counter for later
        c=0
        
        # continue iterating until we find the target
        while True:
        
            # starting index is the middle of the array 
            j = int(round(len(nums)) / 2)
            
            # check if the middle element is the target
            if nums[j] == target:
                return (c + j)
            
            # if 1 element is left then we can return -1 since we have already checked in the previous "if" statement
            elif len(nums) == 1:
                return -1
            
            # if target is in the left half then we set nums equal to the array up until the jth element
            elif nums[j] > target:
                nums = nums[:j]
            
            # if it is in the right side then we set nums to all elements after the jth. Since this will reset j we need a counter to track how many jumps we have made
            else:
                c += j
                nums = nums[j:]