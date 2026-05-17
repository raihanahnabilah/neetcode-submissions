class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Brute force solution:
        # Sort the string
        # See if theyre the same, then group them

        # hash table
        sorted_to_original = {}

        # Build the hash table
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString in sorted_to_original:
                sorted_to_original[sortedString].append(string)
            else:
                sorted_to_original[sortedString] = [string]
        
        # Create the arrays
        return list(sorted_to_original.values())
