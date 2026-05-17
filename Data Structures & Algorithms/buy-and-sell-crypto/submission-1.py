class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 10, 1 
        # 10-1 = -9
        # 1, 5
        # 5-1 = 4
        # 1, 6
        # 6-1 = 5
        # 1, 7
        # 7-1 = 6
        # 1,1
        # 1-1 = 0


        # 10, 8
        # 8-10 = -2
        # 8, 7
        # 7-8 = -1
        # 7, 5
        # 5-7 = -2
        # 5,2
        # 2-5 = -3

        maxVal = 0
        left = 0
        right = 1

        for i in range(1, len(prices)):
            if (prices[right] - prices[left]) < 0:
                left = i
                right = i + 1
            else:
                maxVal = max(maxVal, prices[right] - prices[left])
                right = i + 1
        
        return maxVal

