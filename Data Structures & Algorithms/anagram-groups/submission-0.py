class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution
        # Put a map of reversed -> original 
        # Then for all values that have the same key, we put it in the nested array
        sorted_to_original = {}
        for string in strs:
            reverse_string = "".join(sorted(string))
            if reverse_string in sorted_to_original:
                sorted_to_original[reverse_string].append(string)
            else:
                sorted_to_original[reverse_string] = [string]
        return sorted_to_original.values()
