# Min Cost Climbing Stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @cache
        
        # define a recurring function
        def search(i):
            
            # if 1 step before the end, return cost so far
            if i >= len(cost) - 2:
                return cost[i]
            
            # otherwise find the minimum between the next 2 options
            else:
                return cost[i] + min(search(i+1), search(i+2))
            
        return min(search(0), search(1))