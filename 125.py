# Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Remove edge case
        if len(s) == 1:
            return True
        
        # 2 pointers either end of the string
        l = 0
        r = len(s) - 1
        
        # while pointers have not met or crossed
        while l <= r:
            
            # if left/right pointer is not on a char, keep moving inwards
            if s[l].isalnum() != True:
                l += 1
            elif s[r].isalnum() != True:
                r -= 1
                
            # compare the chars, if equal, move inwards. Otherwise return false
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        
        return True