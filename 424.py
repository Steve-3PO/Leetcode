# Longest Repeating Character Replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # initialise max result, create a count dictionary and a pointer
        max_res = 0
        count = {}
        l = 0
        
        # iterating over s, increment the dictionary corresponding value to the char
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # while we require too many substitions, decrement the current char counter and               move pointer along
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
                
            # calculate max res
            max_res = max(max_res, (r-l+1))
            
        return max_res