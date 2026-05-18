class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 2+-3 = -1. bad?
        # -3+4 = 1. quite good 
        # -3+4+-2 = -1. bad. lets decrement previous one
        # 4+-2 = 2 good.
        # 4+-2+2 = 4. good

        # time complexity: O(n)
        # space complexity: O(1)
        max_val = float("-inf")
        curr_val = 0
        for num in nums:
            curr_val += num
            max_val = max(max_val, curr_val)

            if curr_val < 0:
                curr_val = 0
        
        return max_val


