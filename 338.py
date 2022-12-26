# Counting Bits

class Solution:
    def countBits(self, n: int) -> List[int]:

        # first need an array to count bits
        dfs = [0] * (n + 1)

        # dif is the offset to the nearest full bit number (4, 8...etc)
        dif = 1

        # for all values
        for i in range(1, n + 1):

            # if we are on a full bit number it becomes the new diff
            if dif * 2 == i:
                dif = i 

            # append the increment 
            dfs[i] = 1 + dfs[i - dif]

        return dfs