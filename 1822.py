# Sign of the Product of an Array

class Solution:
    def arraySign(self, nums: List[int]) -> int:

        # we only care about the occurence of negative numbers
        negcount = 0

        # iterating through each vallue
        for num in nums:

            # increment our count if negative
            if num < 0:
                negcount += 1
            
            # if value is 0 we stop since any product with 0 is 0
            if num == 0:
                return 0

        # if at the end we have an even number of negative numbers it must be a positive product, otherwise negative
        if negcount % 2 == 0:
            return 1
        else: return -1
