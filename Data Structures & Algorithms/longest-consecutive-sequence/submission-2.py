class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        res = 0

        for num in setNums:
            if num - 1 in setNums:
                continue
            else:
                currLength = 1
                val = num + 1
                while val in setNums:
                    currLength += 1
                    val += 1
                res = max(res, currLength)
        
        return res
        
