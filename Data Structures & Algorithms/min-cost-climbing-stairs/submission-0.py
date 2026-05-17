class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def recurse(i):
            if i > len(cost)-1:
                return 0
            minCost = min(recurse(i+1), recurse(i+2))
            return minCost + cost[i]

        return min(recurse(0), recurse(1))
    
        