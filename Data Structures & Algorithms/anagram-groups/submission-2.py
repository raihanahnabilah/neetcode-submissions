class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        # # "act", "pots", "tops", "cat", "stop", "hat"

        # # Solution 1: sorting
        # # "act", "pots", "pots", "act", "pots", "hat"
        # # store them in a hashmap
        # # if the sorted version exists in a hashmap, then append them
        
        # sorted_string_to_actual_string = {} # This is O(m)

        # # Overall time complexity: O(m*nlogn)
        # # Overall space complexity: O(m*n)
        # for i, string in enumerate(strs): # O(m) 
        #     copy_of_string = string
        #     # sort:
        #     sorted_string = list(string)
        #     sorted_string.sort() # O(nlogn)
        #     joined_sorted_string = "".join(sorted_string) 
        #     print("check joined", joined_sorted_string)
        #     if joined_sorted_string in sorted_string_to_actual_string: # Worst case: O(n) - average O(1)
        #         sorted_string_to_actual_string[joined_sorted_string].append(copy_of_string)
        #         print("Checker", sorted_string_to_actual_string)
        #     else:
        #         sorted_string_to_actual_string[joined_sorted_string] = [copy_of_string]
        #         print("Checker", sorted_string_to_actual_string)
            
        # # you wanna return all the values
        # # print(sorted_string_to_actual_string.values())
        # return sorted_string_to_actual_string.values()



        # Solution 2
        # instead of sorting, counting the frequency of each characters:

        res = {}
        for string in strs:

            counter = [0] * 26
            for char in string:
                counter[ord(char) - ord('a')] += 1
            
            if tuple(counter) not in res:
                res[tuple(counter)] = [string]
            else:
                res[tuple(counter)].append(string)
        return res.values()




