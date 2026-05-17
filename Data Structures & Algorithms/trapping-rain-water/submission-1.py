class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0

        max_left, max_right = [0] * len(height), [0] * len(height)

        for i in range(len(height) -1):
            curr_left_max = max(max_left[i], height[i])
            max_left[i+1] = curr_left_max
        
        for i in range(len(height)-1, 0, -1):
            curr_right_max = max(max_right[i], height[i])
            max_right[i-1] = curr_right_max
        
        for i, hei in enumerate(height):
            trapped = min(max_left[i], max_right[i]) - hei
            if trapped > 0:
                res += trapped
            
        return res


