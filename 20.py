# Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        # create a dictionary of each pair 
        m = {'(':')', '{':'}','[':']'}
        
        # create a stack to pop and add to
        stack = []
        
        # for each element in s
        for j in s:
            
            # if element is in dictionary we append stack with it
            if j in m:
                stack.append(j)
                
            # if element is not in dictionary, get if there is any elements in stack first then pop and                 element and see if the corresponding dictionary[element] value is equivalent
            elif len(stack) == 0 or m[stack.pop()] != j:
                return False
        
        return len(stack) == 0
        