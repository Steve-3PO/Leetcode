# Average Value of Even Numbers That Are Divisible by Three

class Solution:
    def averageValue(self, nums: List[int]) -> int:

        # two variables, one for the total and the other for count to divide
        total = 0
        count = 0

        # iterate each value in nums, if its divisble by 3 and 2, add it to the total and increment count
        for num in nums:
            if num % 3 == 0 and num % 2 == 0:
                total += num
                count += 1
        
        # must return 0 specifically if not total as 0/0 is wrong
        return (total//count) if total != 0 else 0