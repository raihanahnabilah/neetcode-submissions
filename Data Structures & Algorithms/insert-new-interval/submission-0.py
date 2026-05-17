class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # overlaps with previous and later
        # prev[1] > new[0] = update prev [min(prev[0], new[0]), max(prev[1], new[1])]
        # add prev

        # no-overlaps
        # if prev[1] < new[0]
        # add prev

        res = []
        for i in range(len(intervals)):
            currInterval = intervals[i]
            # in a case where [[1,3]] and new = [4,5]
            # no overlaps
            if currInterval[1] < newInterval[0]:
                res.append(currInterval)
            # in a case where [[6,7]] and new = [1,2]
            elif newInterval[1] < currInterval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [min(currInterval[0], newInterval[0]), 
                                max(currInterval[1], newInterval[1])]
            
        res.append(newInterval) 
        return res

                


