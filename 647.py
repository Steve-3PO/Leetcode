# Palindromic Substrings

class Solution:
    def countSubstrings(self, s: str) -> int:

        # result to increment for each palindrome found
        res = 0

        # we will iterate through each position, treating it as the centre of a palindrome, intialising pointers at the centre
        for i in range(len(s)):
            l = i
            r = i

            # while the pointers are the same character we can move pointers out, this stops looking for palindromes when 2 characters are already not matched
            while (l >= 0 and r < len(s)) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        # repeat for even numbered palindromes
        for i in range(len(s)):
            l = i
            r = i + 1

            while (l >= 0 and r < len(s)) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
                
        return res