class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cache = [-1] * len(cost)

        def recurse(i):
            if i > len(cost)-1:
                return 0
            if cache[i-1] == -1:
                minCost = min(recurse(i+1), recurse(i+2))
                cache[i-1] = minCost + cost[i]
            return cache[i-1]

        return min(recurse(0), recurse(1))
    
        