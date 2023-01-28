# Summary Ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        # going to use a stack to keep current ranges until appended to the result array
        stack = []
        res = []

        # iterate through all of nums
        while nums:

            # take the first number
            p = nums.pop(0)

            # if no number in stack or it is an increment step above the current top stack value we can append
            if not stack or stack and stack[-1] + 1 == p:
                stack.append(p)

            # if not it must have ended the previous range
            else:

                # if stack is not a single number but a range
                if len(stack) > 1:

                    # take the first and last to get the range
                    first = str(stack[0])
                    last = str(stack[-1])

                    # append the required syntax
                    res.append(first+"->"+last)

                    # reset stack as it has moved to res array
                    stack = []

                # if stack is a single value we can just append it as a string to the res array
                else:
                    res.append(str(stack[0]))
                    stack.pop()
                
                # remember to append the new value after resetting the stack
                stack.append(p)

        # incase there is a value/s left in stack after iterating, run the process 1 more time
        if stack:
            if len(stack) == 1:
                res.append(str(stack[0]))
            else:
                first = str(stack[0])
                last = str(stack[-1])
                res.append(first+"->"+last)
                stack = []

        return res