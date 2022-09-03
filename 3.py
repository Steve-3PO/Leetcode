# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # remove edge case
        if len(s) == 0:
            return 0
        
        # starting with 2 pointers at the beginning
        l = 0
        r = 0
        
        # max length defaults to 1, assuming every character is repeated
        max_len = 1
        
        # require a set to determine repeats
        seen = set()
        
        # while not at the end of the string
        while r != len(s):
            
            # if char not in the set, add to set and increment pointer. Recalculate max_len
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                max_len = max(max_len, len(seen))
            
            # if char is in set, recalculate max_len, remove the left point char and increment by 1
            else: 
                max_len = max(max_len, len(seen))
                seen.remove(s[l])
                l += 1
                
                
        return max_len
        