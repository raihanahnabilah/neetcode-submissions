class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution
        # traverse through every single value
        # store the value in a map? maybe value-indices map
        # as we traverse - target - currentnum = res
        # check if our map has that result
        val_to_indices = {}
        res_first = 0
        res_second = 0
        for i, num in enumerate(nums):
            print(num, i)
            if (target - num) in val_to_indices:
                res_second = i
                res_first = val_to_indices[(target-num)]
                break
            else:
                val_to_indices[num] = i
        return [res_first, res_second]
