class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # [3,4,5,6], target = 7
        # 7-3 = 4
        # 3: 0
        # 7-4:3
        #
    
        # Time complexity: O(n)
        # Space complexity: O(n)
        
        num_to_index = {}
        for i, num in enumerate(nums):
            if target - num in num_to_index:
                return [num_to_index[target - num], i]
            else:
                num_to_index[num] = i
        
        return [-1,-1]             