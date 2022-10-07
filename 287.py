class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Identify this is a linked list as every number appears once except 1 number
        # Initialse typical tortoise and hare algorithm
        hare, tortoise = 0, 0
        
        while True:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]
            if tortoise == hare:
                break
            
        tortoise2 = 0
        while True:
            tortoise2 = nums[tortoise2]
            tortoise = nums[tortoise]
            if tortoise == tortoise2:
                break
            
        return tortoise