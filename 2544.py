# Alternating Digit Sum

class Solution:
    def alternateDigitSum(self, n: int) -> int:

        # require a sign variable which will change each value
        sign = 1

        # total to track the combined sum
        total = 0

        # turn number to a string so we can index
        n = str(n)

        # iterate through each character
        for char in n:

            # increment total with appropriate sign sum
            total += (int(char) * sign)

            # change sign
            sign *= -1

        return total