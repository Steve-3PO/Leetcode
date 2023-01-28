# Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # require an array to append our results to
        res = []

        # o(n) solution using 2 pointers, checking for the larger element and appending
        l = 0
        r = len(nums) - 1

        # while we have not crossed pointers
        while l <= r:

            # append the larger of the squares and move the corresponding pointer inwards
            if nums[l]**2 > nums[r]**2:
                res.append(nums[l]**2)
                l += 1
            
            else:
                res.append(nums[r]**2)
                r -= 1
            
        # since we did largest first, we return the reverse of the array
        return res[::-1]