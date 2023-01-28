# Number of Distinct Averages

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:

        # require a set to track unique averages we have seen
        unique = set()

        # since sets have no length variable we can track its length with another variable
        uniquecount = 0

        # sort nums so we can access the next smallest/largest each iteration
        nums = sorted(nums)
        
        # until we cant make a pair
        while len(nums) >= 2:

            # take the smallest from the left and largest from the right of the array
            small = nums.pop(0)
            large = nums.pop(-1)

            # take the average
            average = (large + small)/2

            # if its a new average we add to the set and increment our length tracker
            if average not in unique:
                unique.add(average)
                uniquecount += 1
            
        # return the length variable
        return uniquecount