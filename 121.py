# Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # using two pointers we can track each change, and a profit variable to 
        # keep track of the greatest profit margins
        L = 0
        R = 1
        prof = 0
        
        # while R pointer hasnt reached the end of the list we check if L is
        # great than R, if it is we set L = R as it is a new local minimum
        while R < len(prices):
            if prices[L] >= prices[R]:
                L = R
                
            # otherwise we calculate the profit and check if it is more than
            # any previous profit we calculated
            if prices[L] < prices[R]:
                if (prices[R] - prices[L]) > prof:
                    prof = prices[R] - prices[L]
                    
            # move R along regardless of outcome      
            R += 1
        return prof
    