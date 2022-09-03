# Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # 2 pointers either end of the array
        l = 0
        r = len(height) - 1
        
        # initialise max_volume = 0
        max_volume = 0
        
        # while pointers have not crossed
        while l < r:
            
            # volume is the len x min(height). Calculate max_volume seen so far
            volume = (r - l)*min(height[l], height[r])
            max_volume = max(max_volume, volume)
            
            # move the pointer that has the lower value
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return max_volume
            