class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # permutation?

        result = []
        subset = []

        def dfs(index):
            if index >= len(nums):
                result.append(subset.copy())
                return 

            # Traverse until the last value
            dfs(index + 1)            
            # Append to the result 
            subset.append(nums[index])
            # Traverse again
            dfs(index + 1)
            # Pop the value
            subset.pop()

        
        dfs(0)
        return result

            

            


            
            