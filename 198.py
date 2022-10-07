# House Robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        
        # define a recurrsion function
        def search(i):
            
            # if out of bounds return 0, not None as you cant compare in a max function an int with a None type
            if i == len(nums):
                return 0
            
            # if at the end stop iterating
            elif i == (len(nums) - 2) or i == (len(nums) - 1):
                return nums[i]
            
            # otherwise return the current value and the max between the 2nd and 3rd values along
            else:
                return nums[i] + max(search(i + 2), search(i + 3))
            
        # return the max of the result between starting on index 0 or 1
        return max(search(0), search(1))