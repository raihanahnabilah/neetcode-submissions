class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)

        def recurse(i: int):
            if i >= len(cost):
                return 0
            costPathOne = cost[i] + recurse(i+1)
            costPathTwo = cost[i] + recurse(i+2)
            return min(costPathOne, costPathTwo)
        
        return min(recurse(0), recurse(1))