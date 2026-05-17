class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # def recurse(currTarget: int):
        #     if currTarget == 0:
        #         return 0
        #     if currTarget < 0:
        #         return float("inf")
            
        #     minCoin = float("inf")
        #     for i in range(len(coins)):
        #         totalCoin = 1 + recurse(currTarget - coins[i])
        #         minCoin = min(minCoin, totalCoin)
        #     return minCoin
        
        # res = recurse(amount)
        # return res if res != float("inf") else -1
        
        hashMap = {}

        def recurse(currTarget: int):
            if currTarget == 0:
                return 0
            if currTarget < 0:
                return float("inf")

            # you should check the memoization first
            if currTarget in hashMap:
                return hashMap[currTarget]
            
            minCoin = float("inf")
            for i in range(len(coins)):
                newTarget = currTarget - coins[i]
                totalCoin = 1 + recurse(newTarget)
                minCoin = min(minCoin, totalCoin)
            hashMap[currTarget] = minCoin
            return minCoin
        
        res = recurse(amount)
        return res if res != float("inf") else -1
        