# First Bad Version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # begin with 2 pointers at either end
        L = 0
        R = n
        
        while True:
            
            # midpoint will always be in the center of the L and R pointers
            midpoint = int((L + ((R-L)/2)))
            
            # if the midpoint is True, then reallign R and midpoint
            if isBadVersion(midpoint) == True:
                R = midpoint
                
            # if the midpoint is false, check if its neighbour is True
            # otherwise reallign L and midpoint
            else:
                if isBadVersion((midpoint + 1)) == True:
                    return (midpoint + 1)
                L = midpoint