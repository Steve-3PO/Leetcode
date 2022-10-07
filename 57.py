# Insert Interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # require a result array to append each interval to
        res = []
        
        # looking at each interval at a time
        for i in range(len(intervals)):
            
            # check if the new interval comes before, if it does the rest of the intervals can just be appended
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # or if new interval comes after the current then we append current since it is no longer being used
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                
            # if it overlaps in any way then we take the min and max of both sides, and continue onto the next iteration, we dont append as it could still overlap with more
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res