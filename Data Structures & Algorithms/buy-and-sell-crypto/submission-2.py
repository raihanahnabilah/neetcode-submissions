class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # max profit
        # brute force
        maxProfit = float("-inf")
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                maxProfit = max(maxProfit, prices[j] - prices[i])
        
        if maxProfit < 0:
            return 0
            
        return maxProfit
                
