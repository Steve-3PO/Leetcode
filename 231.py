# Power of Two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # can never be negative or 0
        if n <= 0:
            return False

        # the largest value we can make with a power of 2
        t = 2147483648
        
        # check if there is a remainder as every power of 2 falls into this maximum
        if t % n == 0:
            return True
        else: False