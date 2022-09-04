# Trapping Rain Water

class Solution:
    def trap(self, height: List[int]) -> int:
        
        # if empty list return 0
        if not height:
            return 0

        # initialise 2 pointers either end of the array
        l, r = 0, len(height) - 1
        
        # left max and right max are the largest seen values thus far
        leftMax, rightMax = height[l], height[r]
        
        # res to add to
        res = 0
        
        # while pointers have not crossed
        while l < r:
            
            # increment/decrement the pointer corresponding to the smaller max seen, and calculate new max
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                
                # add the different of the max and the height to the total (total water stored above)
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
                
        return res