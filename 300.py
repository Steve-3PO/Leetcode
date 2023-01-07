# Longest Increasing Subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # dynamic programming solution, array of 0s to map from end to beginning, the longest length it can make
        dp = [0] * len(nums)

        # end number will always take 1
        dp[-1] = 1

        # iterating backwards from the index before -1
        for i in range(len(nums) - 2, -1, -1):
            
            # it will always be 1+ steps
            maxseen = 1

            # check every index after it in the array going forward
            for j in range(i + 1, len(nums)):
                
                # if it forms a sequence, add 1 to its own value of its longest sequence and compare if it is the longest seen
                if nums[i] < nums[j]:

                    maxseen = max(maxseen, 1 + dp[j])
            
            # after checking all values, update the max found
            dp[i] = maxseen
    
        return max(dp)