# K Closest Points to Origin

import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # require a stack, we must append with [distance, x, y] so that when heapify'd, it is sorted in linear time by the first element
        stack = [] 

        # for each pair find the distance to origin then append stack with [distance, x, y]
        for point in points:
            distance = math.sqrt(((point[0]**2) + (point[1]**2)))
            stack.append([distance, point[0], point[1]])

        # use heapify to turn into minheap (min first, max last)
        heapq.heapify(stack)

        # answer must be [x, y] so we require final list to remove distance and iterate k times
        res = []
        while k > 0:
            res.append(heapq.heappop(stack)[1:])
            k -= 1

        return res