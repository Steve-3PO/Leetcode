# Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        
        # use the string so we can reverse
        string = str(abs(x))
            
        # reverse string and covert back to int
        reversed_string = string[::-1]
        val = int(reversed_string)
        
        # check if should be negative and check within bounds
        if x < 0:
            if abs(val) <= (2**31):
                val = -1 * val
                return val
            else:
                return 0
        
        # check if positive and within bounds
        else:
            if val <= ((2**31)-1):
                return val
            else:
                return 0