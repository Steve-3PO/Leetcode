# Fibonacci Number

class Solution:
    def fib(self, n: int) -> int:
        
        @cache
        
        # define a recalling function
        def search(n):
    
            # for the initial values, return 0 and 1
            if n == 1:
                return 1
            if n == 0:
                return 0
            
            # return the addition
            return search(n-1) + search(n-2)
        
        return search(n)