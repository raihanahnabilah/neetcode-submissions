class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        # "act", "pots", "tops", "cat", "stop", "hat"

        # Solution 1: sorting
        # "act", "pots", "pots", "act", "pots", "hat"
        # store them in a hashmap
        # if the sorted version exists in a hashmap, then append them
        
        sorted_string_to_actual_string = {}

        for i, string in enumerate(strs):
            copy_of_string = string
            # sort:
            sorted_string = list(string)
            sorted_string.sort()
            joined_sorted_string = "".join(sorted_string)
            print("check joined", joined_sorted_string)
            if joined_sorted_string in sorted_string_to_actual_string:
                sorted_string_to_actual_string[joined_sorted_string].append(copy_of_string)
                print("Checker", sorted_string_to_actual_string)
            else:
                sorted_string_to_actual_string[joined_sorted_string] = [copy_of_string]
                print("Checker", sorted_string_to_actual_string)
            
        # you wanna return all the values
        print(sorted_string_to_actual_string.values())
        return list(sorted_string_to_actual_string.values())






