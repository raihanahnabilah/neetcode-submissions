class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_index = {}
        for i, num in enumerate(nums):
            if target - num in val_to_index:
                return [val_to_index[target-num], i]
            else:
                val_to_index[num] = i
        
        return -1


