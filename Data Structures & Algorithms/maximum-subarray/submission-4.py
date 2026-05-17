class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [2, -3, 4, -2, 2, 1, -1, 4]
        # 2 = max 2 
        # -1 < 0, lets move on
        # -3 < 0, lets move on
        # 4 = max 4
        # -2 = max 4
        # 4 = max 4
        # 5 = max 5
        # 4 = max 5
        # 8 = max 8

        # [2, -3, 4, -2, 2, 1, -1, 4]
        # lr = 2 = max 2
        # l2 r-3 = -1 < 0 move l to -3 and r to -3
        # l-3 r-3 = -3 < 0 move l to 4 and ro to 4
        # l4 r4 = 4 > 0 move r to -2

        if len(nums) <= 1:
            return nums[0]

        res = float("-inf")
        leftIndex = rightIndex = 0
        currVal = 0

        while rightIndex < len(nums):
            print(leftIndex, rightIndex, nums[leftIndex], nums[rightIndex])
            if leftIndex == rightIndex:
                currVal = nums[leftIndex]
                res = max(res,currVal)
                if currVal < 0:
                    # move left and right index
                    leftIndex += 1
                    rightIndex += 1
                else:
                    # move right index
                    rightIndex += 1
            else:
                currVal += nums[rightIndex]
                res = max(res,currVal)
                if currVal < 0:
                    # move both left and right index to be rightIndex's current value
                    leftIndex = rightIndex
                else:
                    # move right index
                    rightIndex += 1

        return res


                


