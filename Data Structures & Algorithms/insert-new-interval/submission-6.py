class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # [[1,3],[4,6]]
        # new interval: [2,5]

        # 1. 3
        #.  2.  5
        #.     4. 6

        # condition:
        # if list1[1] > newInterval[0]
        # we dont wanna insert and just update newInterval: [1,5]
        
        # if list[1] < newInterval[0]:
        # then insert list1 to result

        # if newInterval[1] < list1[0]:
        # then insert and return entire list

        # time complexity: O(n)
        # space complexity: O(n)

        res = []
        for i, interval in enumerate(intervals):
            if interval[0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif interval[1] < newInterval[0]:
                res.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        
        res.append(newInterval)

        return res

            
