# Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # hashmap to call what we have seen so far
        hashmap = {}
        
        for num in nums:
            
            # add num to hashmap otherwise 0 if not seen yet
            hashmap[num] = 1 + hashmap.get(num, 0)
            
            # stop when occurence is greater than half the length
            if hashmap[num] > (len(nums) / 2):
            
                return num