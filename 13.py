# Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        
        # create a disctionary of all values
        dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
        }
        
        # require a running total and a previous variable
        total = 0
        prev = 0
        
        # for each element in s in reverse order
        for char in s[::-1]:
        
            # if the value is larger than the previous value, we add to the total, and change to the                   current prev value
            if dict[char] >= prev:
                total += dict[char]
                prev = dict[char]
                
            # if the value is smaller, we subtract and reset prev = 0
            else:
                total -= dict[char]
                prev = 0
        
        return total