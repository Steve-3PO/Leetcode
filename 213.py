# House Robber II

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # remove edge case
        if len(nums) <= 3:
            return max(nums)
        
        @cache
        
        # define a recurrsion function, include a true/false input to determine if it started at the first house
        def search(fh, i):
            
            # if out of bounds return 0, not None as you cant compare in a max function an int with a None type
            if i == len(nums):
                return 0
            
            # if at the end stop and the first house was not picked, stop iterating
            elif i == (len(nums) - 2) or (i == (len(nums) - 1) and fh == False):
                return nums[i]
            
            # if started at the first house, determine whether it is better to start at first house or finish at final house
            elif (i == (len(nums) - 1) and fh == True):
                if nums[i] > nums[0]:
                    return nums[i] - nums[0]
                else:
                    return 0
            
            # otherwise return the current value and the max between the 2nd and 3rd values along
            else:
                return nums[i] + max(search(fh, i + 2), search(fh, i + 3))
            
        # return the max of the result between starting on index 0 or 1
        return max(search(True, 0), search(False, 1))