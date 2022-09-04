# Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # remove edge cases
        if len(s) > len(t):
            return 0
        if len(s) == 0:
            return 1
        
        # pointer on s
        l = 0
        
        # iterate through t
        for letter in t:
            
            # if pointer and letter match, increment pointer on s
            if s[l] == letter:
                l += 1
                
                # if l reaches the length of s, end
                if l == len(s):
                    return 1
        
        return 0