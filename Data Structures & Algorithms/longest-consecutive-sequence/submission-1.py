class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
            
        # First clean it, meaning remove it if there are two elements that are the same
        # Convert array to set
        numsSet = list(set(nums))
        # First, sort it
        numsSet.sort()

        res = 1
        current = 1
        for i in range(1, len(numsSet)):
            if numsSet[i] - numsSet[i-1] == 1:
                current += 1 
            else:
                current = 1
            res = max(current, res)
        return res