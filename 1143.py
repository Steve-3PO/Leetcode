# Longest Common Subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # create a grid of 0's of (m + 1)(n + 1), we will work backwards with a dp solution. When chars match we move up and left to the origin adding 1, when they dont match we want to take the maximum possible length between the top and left possibilities
        dp = [[0 for x in range(len(text2) + 1)] for y in range(len(text1) + 1)]

        # going backwards through the height
        for x in range(len(text1) - 1, -1, -1):

            # through each row
            for y in range(len(text2) - 1, -1, -1):
                
                # if they are equal to eachother, we add 1 to the value down and right of it, 0s are set at edges by default
                if text1[x] == text2[y]:
                    dp[x][y] = dp[x + 1][y + 1] + 1

                # otherwise we take the max of both directions, to the right or below the current index
                else:
                    dp[x][y] = max(dp[x + 1][y], dp[x][y + 1])
                    
        # we know the origin has the maximum value that has been found through the array   
        return dp[0][0]