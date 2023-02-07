# Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # we will use two pointers, the left pointer will increment by 1 from the start everytime a swap is made, the right pointer will go through finding only the numbers that arent 0 and swapping them with the left position
        l = 0
        
        # iteration through the array
        for r in range(len(nums)):

            # when we have found the next item in its relative order we move it to the nums[l] position
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]

                # increment l so that we have the next target position ready for the next right pointer number
                l += 1
        
        return nums

            