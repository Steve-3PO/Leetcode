# Count the Digits That Divide a Number

class Solution:
    def countDigits(self, num: int) -> int:

        # variable to track number of divisible digits
        total = 0

        # iterate through digits in string num, as int not possible
        for digit in str(num):

            # when divisible with no remainder, increment the counter
            if num % int(digit) == 0:
                total += 1
                
        return total