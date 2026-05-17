class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)

        if len(piles) >= h:
            return right
        
        # brute force:
        # h >= sum(piles) / x
        # x >= some value -> so we know it should be larger than that value

        left = math.ceil(sum(piles) / h)
        res = right

        while left <= right:
            middle = (left + right) // 2
            currRes = 0
            for pile in piles:
                currRes += math.ceil(pile/middle)
            if currRes <= h:
                res = min(res, middle)
                right = middle - 1
            else:
                left = middle + 1
        return res
        

        # for i in range(lowestPotentialRes, highestRes+1):
        #     currRes = 0
        #     for pile in piles:
        #         currRes += math.ceil(pile / i)
        #     res = min(res, i if currRes <= h else float("inf"))
        # return res





        