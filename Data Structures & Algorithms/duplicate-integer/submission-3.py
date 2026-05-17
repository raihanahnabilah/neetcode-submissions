class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isSeen = set()
        for num in nums:
            if num not in isSeen:
                isSeen.add(num)
            else:
                return True
        
        return False
    

            