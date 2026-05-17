class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Potential solution - 1 - brute force
        # I would create a map -> O(n)
        # Will increment the values in the map
        # If the value > 1 -> then return true

        # A set of value that I have encountered? 
        # If the value is in the set, then return true?
        setValue = set(); # O(1)
        for num in nums: # O(n)
            if num in setValue:
                return True
            else:
                setValue.add(num)
        return False

