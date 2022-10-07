# Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort intervals by first value
        intervals.sort(key=lambda pair: pair[0])
        
        # create a result array and add first element, this way we can continue adding or changing the first index in place with a for loop
        res = [intervals[0]]
        
        # interate though every value
        for i in range(1,len(intervals)):
            
            # if the last value of the last appended result array and the first value of the list array are merged 
            if intervals[i][0] <= res[-1][1]:
                
                # update the new boarders
                res[-1][0] = min(res[-1][0], intervals[i][0])
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                
                #otherwise append the non merged array
                res.append(intervals[i])
                
        return res