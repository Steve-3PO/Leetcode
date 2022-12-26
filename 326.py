# Power of Three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        # whatever value of n has to be greater than 0 and a factor of the larger power of 3 possible which is 3 ** 20
        return n > 0 and 3**20 % n == 0