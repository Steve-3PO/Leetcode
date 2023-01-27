# Maximum Count of Positive Integer and Negative Integer

class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        # counters to track occurence of values
        neg = 0
        pos = 0

        # iterate through the list
        for num in nums:

            # increment counters depending on if num is positive or negative
            if num < 0:
                neg += 1
            elif num > 0:
                pos += 1
                
        # return the max value
        return max(neg, pos)