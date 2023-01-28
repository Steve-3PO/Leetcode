# N-th Tribonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:

        # initialise a list with the first parameters given
        dp = [0]
        dp.append(1)
        dp.append(1)

        # check if we need to continue
        if n < 3:
            return dp[n]

        # keep iterating until n is complete, returning the last index
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
        
        return dp[n]