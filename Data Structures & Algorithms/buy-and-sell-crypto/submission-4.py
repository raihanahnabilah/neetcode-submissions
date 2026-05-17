class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # # max profit
        # # brute force: O(n^2)
        # maxProfit = float("-inf")
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         maxProfit = max(maxProfit, prices[j] - prices[i])
        
        # if maxProfit < 0:
        #     return 0

        # return maxProfit
                
        
        # more optimized method
        # [10, 1] = 1-10 = -9
        # [1,5] = 5-1 = 4
        # [1,6] = 6-1 = 5
        # [1,7] = 7-1 = 6
        # [1,1] = 1-1 = 0 
        
        # time complexity: O(n)
        # space complexity: O(1)
        maxProfit = 0

        if len(prices) <= 1:
            return maxProfit

        left_pointer = 0
        right_pointer = 1
        
        while left_pointer < len(prices) and right_pointer < len(prices):
            maxProfit = max(maxProfit, prices[right_pointer] - prices[left_pointer])
            if prices[right_pointer] - prices[left_pointer] < 0:
                left_pointer = right_pointer
                right_pointer += 1
            else:
                right_pointer += 1
        return maxProfit                





