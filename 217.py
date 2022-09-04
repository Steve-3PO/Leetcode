# Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # create a set
        seen = set()
        
        # if item isnt in set, add it
        for item in nums:
            if item not in seen:
                seen.add(item)
                
            # return true if it appears in set
            else:
                return True
        return False