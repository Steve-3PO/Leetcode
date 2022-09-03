# Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Using a hashmap to improve lookup time
        hashmap = {}
        
        # Iterate through each element
        for i, num in enumerate(nums):
            
            # If we have come across the necessary number to make the target already it will be in hashmap
            if (target - num) in hashmap:
                
                return hashmap[(target - num)], i
                
            # Otherwise we add num to hashmap, so that its available for other iterations 
            else: 
                hashmap[num] = i