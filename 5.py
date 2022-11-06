# Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # to track the string with longest length
        maxsubstring = ""
        length = 0
        
        # treat every index as the center of a palindrome
        for i in range(len(s)):
            l = i
            r = i
            
            # odd length iteration, continue going out until it is no longer a palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = (r - l + 1)
                if curr > length:
                    length = curr
                    maxsubstring = s[l:r+1]
                l -= 1
                r += 1
                
                
            l = i
            r = i + 1
            
            # even length as l, r start 1 index apart
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = (r - l + 1)
                if curr > length:
                    length = curr
                    maxsubstring = s[l:r+1]
                l -= 1
                r += 1
                
        return maxsubstring