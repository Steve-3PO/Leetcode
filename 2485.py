# Find the Pivot Integer

class Solution:
    def pivotInteger(self, n: int) -> int:
        
        # initialise step, left and right sides of the list
        prev = 1
        left = 1
        right = sum(range(1, n + 1))

        # can stop when left is no longer smaller, either stopping when they are equal or not
        while left < right:
            
            # when moving to next integer to check, right loses the previous int first
            right -= prev

            # left gains the next integer on after previous (e.g moving 2 -> 3, prev = 2, left += 3)
            left += prev + 1

            # adjust for next integer
            prev += 1

        # check if stop occurred when equal
        if left == right:
            return prev
        else:
            return -1