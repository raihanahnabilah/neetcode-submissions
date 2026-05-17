class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Solution 1 - flatten the nested array into one array?
        flattenMatrix = [x for xs in matrix for x in xs]
        # then do binary search here:
        left = 0
        right = len(flattenMatrix) - 1
        while left <= right:
            middle = (left + right) // 2
            if flattenMatrix[middle] == target:
                return True
            elif flattenMatrix[left] == target:
                return True
            elif flattenMatrix[right] == target:
                return True
            elif flattenMatrix[middle] > target:
                right = middle - 1
            elif flattenMatrix[middle] < target:
                left = middle + 1
        return False

