# Last Stone Weight

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # make stones negative so that the heap is reverse, larger magnitude numbers at the bottom
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        # while there are multiple stones
        while len(stones) > 1:
            
            # pop 2 stones
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            # if second is larger, calculate the difference, otherwise you know first is larger due to the heap
            if second > first:
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        
        return abs(stones[0])