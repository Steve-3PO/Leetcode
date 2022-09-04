# Koko Eating Bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # left a right bounds are 1 and max of the stacks
        l, r = 1, max(piles)
        k = 0

        # while searching calculate a midpoint
        while l <= r:
            m = (l + r) // 2

            # initialise total time
            totalTime = 0
            
            # for each stack in piles
            for p in piles:
                
                # add the time it would take to eat
                totalTime += ((p - 1) // m) + 1
                
            # if eating is too fast, reduce eating speed by moving right pointer in, and vice versa
            if totalTime <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k