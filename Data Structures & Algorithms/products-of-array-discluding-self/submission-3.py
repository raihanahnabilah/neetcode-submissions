class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        # nested for loop
        res = []
        for i in range(len(nums)):
            eachVal = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                eachVal *= nums[j]
            res.append(eachVal)
        return res