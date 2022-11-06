# Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # result and carry necessary
        result = ""
        carry = 0
        
        # to pop values we must turn strs to lists
        a = list(a)
        b = list(b)
        
        while a or b or carry:
            
            # checks if a and b are usuable, adding to carry
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            
            # carry ranges 0-3, therefore modulus of 2 will set to the correct value
            result += str(carry % 2)
            
            # if carry = 2/3 then carry turns to 1
            carry //= 2
            
        return result[::-1]
                 