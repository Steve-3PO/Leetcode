# Minimum Cuts to Divide a Circle

class Solution:
    def numberOfCuts(self, n: int) -> int:
        
        # for even number of pieces you make half the cuts
        if n % 2 == 0:
            return (n//2)
        
        # edge case for 1 piece requiring no cuts
        elif n == 1:
            return 0

        # otherwise odd number pieces require the same amount of cuts
        else:
            return n