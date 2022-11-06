# Sqrt(x)

import math

class Solution:
    def mySqrt(self, x: int) -> int:
        
        # we know there must be an upper and lower limit of a possible square root based off of the number of digits in the squared number
        n = len(str(x))
        m = ceil(n / 2)
        
        lowerlimit = 10 ** (m - 1)
        
        # using the lower and upper limit, find the value where square root exists
        while True:
            curr = lowerlimit * lowerlimit
            if curr == x:
                return lowerlimit
            elif curr > x:
                return lowerlimit - 1
            lowerlimit += 1