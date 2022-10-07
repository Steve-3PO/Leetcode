# Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # require a current sum and a maxseen so far, this is set as the first array as we cant initialise as 0
        curr = 0
        maxseen = nums[0]
       
        
        for num in nums:
            
            # add the num to current and calculate the new current total
            curr += num
            
            # update the new max seen
            maxseen = max(curr, maxseen)
            
            # if it is less than 0 we can reset and begin again
            if curr <= 0:
                curr = 0
                
        return maxseen