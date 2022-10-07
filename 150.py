# Evaluate Reverse Polish Notation

import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # require a stack and a dictionary of operators
        stack = []
        operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        
        # iterate through given list until an operator is found
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                
                # pop the last 2 numbers and use the dictionary to access the operator not in string format
                num2 = stack.pop()
                num1 = stack.pop()
                total = operators[token](num1, num2)
                
                # round towards 0 to remove edge cases of negligible numbers
                if total < 0:
                    total = ceil(total)
                else:
                    total = floor(total)
                    
                # append the total to the stack
                stack.append(total)
                
        # return the last number in the stack
        return stack.pop()