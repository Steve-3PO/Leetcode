# Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # cant have a palindrome if there is a negative sign
        if x < 0: return False
        
        # convert to str
        x = str(x)
        
        # 2 pointers starting beginning and end of the string
        l = 0
        r = len(x) - 1
        
        # while not met or passed, if chars are the same, carry on incrementing and decrementing
        while l < r:
            if x[l] == x[r]:
                l += 1
                r -= 1
            else:
                return False
        return True