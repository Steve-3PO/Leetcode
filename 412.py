# Fizz Buzz

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        output = []
        
        # incrementing and checking which which are divisible by 3 and 5
        for i in range(1, n + 1):
            
            # and
            if i % 3 == 0 and i % 5 == 0:
                output.append("FizzBuzz")
                
            # or
            elif i % 3 == 0 and i % 5 != 0:
                output.append("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                output.append("Buzz")
                
            # otherwise append just the number
            else:
                output.append(f"{i}")
                
        return output