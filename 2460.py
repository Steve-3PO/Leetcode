# Apply Operations to an Array

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        # require 2 variables, i to index nums, zero count to keep track of the no. of 0's
        i = 0
        zerocount = 0

        # iterate until we have reached the end of the list
        while i < len(nums) - 1: 

            # if a number is 0, instantly remove and add to the zero count
            if nums[i] == 0:
                zerocount += 1
                nums.pop(i)

            # if its not a zero determine if it fits the criteria, if it does we make the change and move along
            elif nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                i += 1

            # if not zero or fit criteria we can just move along
            else:
                i += 1

        # add 0's equal to the no. taken out
        for j in range(zerocount):
            nums.append(0)

        return nums