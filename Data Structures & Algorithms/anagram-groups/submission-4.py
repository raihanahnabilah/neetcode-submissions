class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Brute force solution:
        # Sort the string
        # See if theyre the same, then group them

        # # hash table
        # sorted_to_original = {} # Space complexity: O(n) - worst case scenario

        # # Build the hash table - overall: O(n^3logn)
        # for string in strs: # O(n)
        #     sortedString = "".join(sorted(string)) # O(nlogn) sorted
        #                                             # O(n) .join
        #                                             # O(n^2logn)
        #     if sortedString in sorted_to_original:
        #         sorted_to_original[sortedString].append(string)
        #     else:
        #         sorted_to_original[sortedString] = [string]
        
        # # Create the arrays
        # return list(sorted_to_original.values())

        # Non brute-force solution
        alphabetcounter_to_value = {}

        for string in strs:
            string_mapper = [0] * 26
            for char in string:
                string_mapper[ord(char) - ord('a')] += 1
            string_mapper_tuple = tuple(string_mapper)

            if string_mapper_tuple in alphabetcounter_to_value:
                alphabetcounter_to_value[string_mapper_tuple].append(string)
            else:
                alphabetcounter_to_value[string_mapper_tuple] = [string]

        return list(alphabetcounter_to_value.values())









