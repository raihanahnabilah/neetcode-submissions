class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        #  index = 0
        # +1
        # index = 1
        # +1. +2
        # index = 2 index = 3
        # + 0        + 1
        # False       index = 4
        #               True

        res = False
        # Solution 1: with recursion
        def dfs(index):
            nonlocal res
            # Base case:
            if len(nums) - 1 == index:
                return True
            if nums[index] == 0:
                return False
            # Recursive case
            for i in range(nums[index] + 1):
                if i == 0:
                    continue
                res = res or dfs(index + i)
            return res
        # First index
        return dfs(0)








