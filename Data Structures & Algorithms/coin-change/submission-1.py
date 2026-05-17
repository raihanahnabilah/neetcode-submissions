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
            
            minCoin = float("inf")
            for i in range(len(coins)):
                indexPos = currTarget - coins[i]
                if indexPos not in hashMap:
                    calculateCoin = recurse(indexPos)
                    hashMap[indexPos] = calculateCoin
                totalCoin = 1 + hashMap[indexPos]
                minCoin = min(minCoin, totalCoin)
            return minCoin
        
        res = recurse(amount)
        return res if res != float("inf") else -1
        