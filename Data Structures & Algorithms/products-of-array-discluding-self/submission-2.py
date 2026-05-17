class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solutions:
        # Using like nested for loop?
        
        # result = []

        # # But this is O(n^2)
        # for i, mainNum in enumerate(nums):
        #     productRes = 1
        #     copyNums = nums.copy()
        #     copyNums.pop(i)
        #     for j, secNum in enumerate(copyNums):
        #         productRes *= secNum
        #     result.append(productRes)

        # return result

        # The prefix and suffix solution
        # [1,2,4,6]
        # prefix: [1,1,2,8]
        # suffix: [48,24,6,1]

        prefixArray = []
        for i, num in enumerate(nums):
            if i == 0:
                prefixArray.append(1)
            else:
                productResult = nums[i-1] * prefixArray[i-1]
                prefixArray.append(productResult)

        suffixArray = []
        for i, num in enumerate(reversed(nums)):
            if i == 0:
                suffixArray.append(1)
            else:
                productResult = nums[len(nums)-i] * suffixArray[i-1]
                suffixArray.append(productResult)
        suffixArray = reversed(suffixArray)

        result = []
        for x, y in zip(prefixArray, suffixArray):
            result.append(x * y)

        return result






        