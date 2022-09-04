# Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # edge case elimination
        if n == 1:
            return 1
        
        # fibonachi sequence
        list = [1,1]
        
        # compute next numbers
        for i in range(2, n+1):
        
            list.append(list[i-1] + list[i-2])
            
        # return nth item
        return list[n]