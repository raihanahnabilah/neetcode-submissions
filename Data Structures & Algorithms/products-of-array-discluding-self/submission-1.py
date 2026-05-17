class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solutions:
        # Using like nested for loop?
        
        result = []

        # But this is O(n^2)
        for i, mainNum in enumerate(nums):
            productRes = 1
            copyNums = nums.copy()
            copyNums.pop(i)
            for j, secNum in enumerate(copyNums):
                productRes *= secNum
            result.append(productRes)

        return result




        