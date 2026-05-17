class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        list_nums = list(set_nums)
        
        res = 0
        curr = 1
        for num in list_nums:
            if num - 1 in set_nums: 
                continue # this is to not repeat the previou count
            else: 
                iterate = num + 1
                while iterate in set_nums:
                    curr += 1
                    iterate += 1
                res = max(curr, res)
                curr = 1
        return res


