class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Brute force solution:
        # Sort the string
        # See if theyre the same, then group them

        # # hash table
        # sorted_to_original = {} # Space complexity: O(j) - worst case scenario is length of array

        # # Build the hash table - overall: O(jklogk)
        # for string in strs: # O(j) - length of array 
        #     sortedString = "".join(sorted(string)) # O(klogk) sorted
        #     if sortedString in sorted_to_original:
        #         sorted_to_original[sortedString].append(string)
        #     else:
        #         sorted_to_original[sortedString] = [string]
        
        # # Create the arrays
        # return list(sorted_to_original.values())

        # Non brute-force solution
        alphabetcounter_to_value = {} # Space complexity: O(j) - worst case scenario is length of array

        # Overall on this part: O(jk)
        for string in strs: # O(j) - length of the array
            string_mapper = [0] * 26 # Space complexity: O(26) -> constant -> O(1)
            for char in string: # O(k) - length of the longest string
                string_mapper[ord(char) - ord('a')] += 1
            string_mapper_tuple = tuple(string_mapper) # O(1)

            if string_mapper_tuple in alphabetcounter_to_value:
                alphabetcounter_to_value[string_mapper_tuple].append(string)
            else:
                alphabetcounter_to_value[string_mapper_tuple] = [string]

        return list(alphabetcounter_to_value.values()) # O(1)









