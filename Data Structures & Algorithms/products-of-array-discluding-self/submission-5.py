class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,1,2,8]
        # [48,24,6,1]

        # optimized method
        leftToRightArr = []
        leftToRight = 1
        leftToRightArr.append(leftToRight)
        for i in range(len(nums)-1):
            leftToRight *= nums[i]
            leftToRightArr.append(leftToRight)

        rightToLeftArr = [0] * len(nums)
        rightToLeft = 1
        rightToLeftArr[len(nums)-1] = rightToLeft
        # print(rightToLeftArr)
        for i in range(len(nums)-1, 0, -1):
            # print("Check numsi", nums[i])
            rightToLeft *= nums[i]
            rightToLeftArr[i-1] = rightToLeft
            # print("int righttoleft", rightToLeftArr)
        
        # print("lefttoright", leftToRightArr)
        # print("righttoleft", rightToLeftArr)

        res = []
        for left, right in zip(leftToRightArr, rightToLeftArr):
            res.append(left*right)
        return res





        # # brute force method
        # # nested for loop - O(n^2) time complexity, O(n) space complexity
        # res = []
        # for i in range(len(nums)):
        #     eachVal = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         eachVal *= nums[j]
        #     res.append(eachVal)
        # return res

        ## the solution below doesnt work
        # # another method:
        # # eventually just need to multiply all, then divide by current val
        # total = 1
        # zeroExists = False
        # for num in nums:
        #     if num == 0:
        #         zeroExists = True
        #         continue
        #     else:
        #         total *= num
        # res = []
        # for num in nums:
        #     if zeroExists:
        #         if num == 0:
        #             res.append(total)
        #         else:
        #             res.append(0)
        #     else:
        #         res.append(total//num)
        # return res


