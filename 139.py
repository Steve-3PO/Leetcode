# Word Break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Dynamic programming solution, create array of length s + 1 and fill with False by default
        dp = [False] * (len(s) + 1)

        # last index will be True as it completes the word
        dp[len(s)] = True

        # iterate backwards each step
        for i in range(len(s) - 1, - 1, - 1):

            # going through each word possible
            for word in wordDict:

                # if the word fits without exceeding index limit, and matches itself within the string, then we can link it with the position ahead of it by the length of the word
                if (i + len(word) <= len(s)) and (s[i:(i + len(word))] == word):
                   dp[i] = dp[i + len(word)]

                # when a fit has been found we can stop
                if dp[i]:
                    break
        
        # returning the first index will return the link to the end if true
        return dp[0]