class Solution:
    def trap(self, height: List[int]) -> int:
        
        # 0 -> cant do anything
        # 2 -> max = 2 -> cant insert anything
        # 0 -> can have something here depending on what the value next is -> min(before, after)
        # 3 -> max = 3


        # 3 -> max = 3
        # 1 -> max = 3 -> can have something here but depends on the value later -> min between before and after = 3 -> 3 - 1 = 2
        # 0 -> max = 3 -> can have something here but depends on the value later -> min between before and after = 3 -> 
        # 1 -> max = 3 -> can have omething here but depends on the value later
        # 3 -> max = 3 -> 

        maxLeft = []
        maxLeftVal = 0
        for num in height:
            maxLeft.append(maxLeftVal)
            maxLeftVal = max(maxLeftVal, num)

        maxRight = [0] * len(height)
        maxRightVal = 0
        for i in range(len(height)-1, -1, -1):
            maxRight[i] = maxRightVal
            maxRightVal = max(maxRightVal, height[i])
        
        # [0,0,2,2,3,3,3,3,3,3]
        # [3,3,3,3,3,3,3,2,1,0]
        
        # h[i] = 0 -> left = 0, right = 3 -> null
        # h[i] = 2 -> left = 0, right = 3 -> null
        # h[i] = 0 -> left = 2, right = 3 -> min(left, right) - h[i] = 2
        
        res = 0
        for i in range(len(height)):
            if maxLeft[i] == 0 or maxRight[i] == 0:
                continue
            curr = min(maxLeft[i], maxRight[i]) - height[i]
            if curr > 0:
                res += curr
        return res
