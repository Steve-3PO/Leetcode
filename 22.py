# Generate Parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # require a result to append possible combinations
        res = []

        # since we do not use simultaneous stacks we only need one that we pop from after using, as we backtrack
        stack = []

        # our function will take only how many open and close brackets there are
        def search(ob, cb):

            # we can append the possible result when we have used all brackets
            if ob == cb == n:
                res.append("".join(stack))
                return
            
            # default to using an open bracket first until n is met
            if ob < n:

                # append stack and run new search function
                stack.append("(")
                search(ob + 1, cb)

                # remember to pop as it backtracks
                stack.pop()

            # close brackets can only be used if less than the number of open
            if cb < ob:

                # append and run new search
                stack.append(")")
                search(ob, cb + 1)

                # remember to pop
                stack.pop()
        
        search(0, 0)
        return res