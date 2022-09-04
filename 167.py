# Two Sum II - Input Array Is Sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # start with 2 pointers either end of the list
        l = 0
        r = len(numbers) - 1
        
        # continue iterating
        while True:
            
            # if total of pointers is too large, move right pointer in
            if numbers[l] + numbers[r] > target:
                r -= 1
            
            # if total of pointers is too small, move left pointer in
            elif numbers[l] + numbers[r] < target:
                l += 1
                
            # return indexes
            else:
                return [l+1, r+1]