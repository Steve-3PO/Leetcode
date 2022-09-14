# Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # starting with a pointer at the end index
        n = len(digits) - 1
        
        # while we can iterate
        while n != -1:
            
            # if the current number is not 9, just add one and return digits
            if digits[n] != 9:
                digits[n] += 1
                return digits
            
            # if it is 9, set the new number to 0, decrement n and check if we are at the start of the array yet
            else:
                digits[n] = 0
                n -= 1
                if n == -1:
                    return [1] + digits