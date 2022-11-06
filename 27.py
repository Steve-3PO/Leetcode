# Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # as the array will be changed we cannot use a for loop, must use pointer
        pointer = 0
        
        # for the entire list, and so long as there is a value to check
        while pointer < len(nums) and nums is not None:
            
            # remove value if it is the same
            if nums[pointer] == val:
                nums.pop(pointer)
            
            # otherwise move along list
            else:
                pointer += 1