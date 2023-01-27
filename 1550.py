# Three Consecutive Odds

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        # going to use a stack to append odd valies while each new value is odd
        stack = []

        # until we can no longer make a length of 3 string, or if stack has reached 3 in length
        while (len(arr) + len(stack) >= 3) and len(stack) < 3:

            # take new value
            new = arr.pop(0)

            # for even numbers we reset stack
            if new % 2 == 0:
                stack = []

            # for odd we add the new number
            else:
                stack.append(new)

        # check if we stopped because we got 3 odd numbers in a row
        return len(stack) == 3