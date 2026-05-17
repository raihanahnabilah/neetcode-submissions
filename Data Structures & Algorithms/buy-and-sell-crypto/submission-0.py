class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Basically, traverse through the array
        # Then if you found a value that is lower than your current lower -> store it
        # And then subtract the current lowest with the current value youre in -> store it
        # As you traverse, if the subtraction becomes larger -> store them

        lowest = 1001 # since 0 <= prices[i] <= 100
        profit = -1
        for i, price in enumerate(prices):
            if price < lowest:
                lowest = price
            curr = price - lowest
            if curr > profit:
                profit = curr
        return profit


        