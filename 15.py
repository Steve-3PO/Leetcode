# 3 Sum

import math as mt

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort numbers first
        nums.sort()
    
        # empty array to append to
        ans = []
        
        # for each element in the array
        for i, item in enumerate(nums):
            
            # if on a repeat number, continue
            if i > 0 and item == nums[i - 1]:
                continue
                
            # otherwise start two pointers, ahead by 1 and at the end
            l = i + 1
            r = len(nums) - 1
                
            # while pointers not crossed. Increment the left pointer or decrement the right if the total is             too small or too large respectively
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                    
                # otherwise append the indexes 
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    
                    # if on a repeat, continue incrementing till a new value is found
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return ans  