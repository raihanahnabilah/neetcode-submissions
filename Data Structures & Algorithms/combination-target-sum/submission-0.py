class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []

        def dfs(index, subset, totalCount):
            if totalCount == target:
                result.append(subset.copy())
                return

            if index >= len(nums) or totalCount > target:
                return

            # adding its own number
            subset.append(nums[index])
            dfs(index, subset, totalCount + nums[index])

            # not adding its own number - move on to the next one
            subset.pop()
            dfs(index + 1, subset, totalCount)


        dfs(0, [], 0)
        return result
