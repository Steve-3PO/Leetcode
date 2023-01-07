# Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # to remove edge cases, have the max value as the result by default
        res = max(nums)

        # these will track the max and min we have seen along the way, with a min and max we can just track these rather than the signs of the nums
        maxseen = 1
        minseen = 1

        # iterating through each num
        for num in nums:

            # as we need the current maxseen after we change it we can store in a temp variable
            tmp = maxseen

            # calculate the maxseen, this could be from just the number itself, num * maxseen (if both positive), num * minseen (if both negative)
            maxseen = max(num, maxseen * num, minseen * num)

            # same logic for minseen using the temp variable
            minseen = min(num, tmp * num, minseen * num)

            # change the result each step to track
            res = max(res, maxseen)

        return res