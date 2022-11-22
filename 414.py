# Third Maximum Number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        # sort the numbers in descending order
        nums = sorted(nums, reverse = True)
        
        # create set for unique values
        seen = set()
        
        # iterate through numbers descending
        for num in nums:

            # if not seen add to set, stop after 3 elements in set
            if num not in seen:
                seen.add(num)
                
                if len(seen) == 3:
                    return num
                
        # if not 3 elements exist then return largest number
        return nums[0]