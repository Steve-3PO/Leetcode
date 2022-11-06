# Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # continue until nums2 is empty
        while nums2 != []:
            
            # starting at the first index, pop a num2 element
            pointer = 0
            curr = nums2.pop()
            
            # continue until you find where curr fits, must stop before the list of 0s after index m
            while curr > nums1[pointer] and pointer < m:
                pointer += 1
            
            # insert the value at the index found
            nums1.insert(pointer, curr)
            
            # remove a 0 from the end of nums1
            nums1.pop()
        
        return nums1