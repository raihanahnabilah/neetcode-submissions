class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Choice: either add the num value or add []

        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i] - give value
            subset.append(nums[i])
            dfs(i+1)
            # decision not to include nums[i] - give empty subset
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res
