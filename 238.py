# Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # create 2 arrays of 1s
        ar1 = [1] * len(nums)
        ar2 = [1] * len(nums)
        
        # multiplication factor
        a, b = 1, 1
        
        # for each space in the array, set as the product of the multiplication of itself           and the factors before it
        for i in range(len(nums)):
            a = a * nums[i]
            ar1[i] = a
        
        # same for array b in reverse
        for i in range(len(nums)-1, -1, -1):
            b = b*nums[i]
            ar2[i] = b
            
        # iterate through the nums array
        for i in range(len(nums)):
            
            # in the 0th index, can take the 1st index of array b
            if i == 0:
                nums[i] = ar2[i+1]
                
            # in the last index, can take the penultimate index of array a
            elif i == (len(nums) - 1):
                nums[i] = ar1[i-1]
                
            # otherwise multiple values either side of index, from the corresponding arrays
            else:
                nums[i] = ar1[i-1] * ar2[i+1]
        return nums