class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        list_nums = list(set_nums)
        print("checking list_nums", list_nums)
        
        res = 0
        curr = 1
        for num in list_nums:
            val = num+1
            while val in set_nums:
                curr += 1
                val += 1
            res = max(curr, res)
            curr = 1
        return res


