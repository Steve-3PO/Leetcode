# Jump Game

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # require a jump to start at the back and work forward
        jump = 1

        # while we have not minimised nums to length of 1
        while len(nums) > 1:

            # return false if jump required is larger than the length of nums
            if jump > len(nums) - 1:
                return False

            # if the jump required from the second last element is possible, shorten the array and set jumps to 0
            if nums[-1 - jump] >= jump:
                nums = nums[: -jump]
                jump = 1 

            # otherwise we require a larger jump
            else:
                jump += 1

        return True