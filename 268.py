# Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # a number will be missing between 0,1,2,3...len(nums) vs nums
        # every i value will have a corresponding num[i] except the only number thats missing. e.g. if number 3 is missing, the index 3 will never be subtracted since nums[i] never equals 3 
        # Must start with len(nums) as the range array is 1 value smaller
        res = len(nums)
        
        for i in range(len(nums)):
            res += i - nums[i]
            
        return res