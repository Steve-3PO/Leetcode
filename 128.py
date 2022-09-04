# Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # create a set of nums (instant lookup time) and a variable to track longest seq.
        numSet = set(nums)
        longest = 0

        # iterate through the array
        for n in nums:

            # check if its the start of a sequence, if it is, initialise length
            if (n - 1) not in numSet:
                length = 1

                # while n + 1 exists, continue calculating max length
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
