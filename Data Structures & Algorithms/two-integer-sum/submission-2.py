class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force: you do for-loop with two pointers
        # Time complexity: O(n^2)

        # Non-brute force:
        # Traverse through every single value
        # store the value that it has seen in the dictionary
        val_to_index = {}

        for i, num in enumerate(nums):
            if target - num in val_to_index:
                return [val_to_index[target-num], i]
            else:
                val_to_index[num] = i
        


