# Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        
        # need a set to know if we have seen a value before
        seen = set()
        
        # while we havent reached n = 1
        while n != 1:
            
            # add current n to set
            seen.add(n)
            
            # new n is the sum of its components squared
            n = sum([int(x)**2 for x in str(n)])
            
            # check if n is in seen
            if n in seen: return False
            
        return True