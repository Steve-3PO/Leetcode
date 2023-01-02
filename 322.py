# Coin Change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # create an array of length(amount) so that we can track how many coins it takes to get to each value
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # check for each value up to amount + 1
        for i in range(1, amount + 1):

            # going through each coin
            for coin in coins:

                # if subtracting the given coin is possible
                if i - coin >= 0:

                    # set the new minimum required coins to reach that value
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        # check if it was possible using the array of default values
        return dp[amount] if dp[amount] != amount + 1 else -1