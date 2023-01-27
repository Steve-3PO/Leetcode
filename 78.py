# Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # backtracking solution requires a final res array and a stack which we will add and pop from each iteration
        res = []
        stack = []

        # create a function that passes in an index to track, each value can either be included or not included
        def search(i):

            # when we reach the end then we add stack to the res
            if i == len(nums):
                res.append(stack.copy())
                return
            
            # append the current value and perform a search with the new stack
            stack.append(nums[i])
            search(i + 1)

            # after this backtracks we pop the stack and carry on with calling the function with an empty stack
            stack.pop()
            search(i + 1)

        search(0)

        return res