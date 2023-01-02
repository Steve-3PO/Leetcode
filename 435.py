# Non-overlapping Intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # sort by starting value
        intervals = sorted(intervals)

        # first interval can be appended instantly
        res = [intervals[0]]
        
        # iterating through each interval after the first initially appended
        for start, end in intervals[1:]:

            # if the next interval starts after the last in res ends, we can just append
            if res[-1][1] <= start:
                res.append([start, end])

            # if they are overlapping, only change last appended if the new interval ends sooner
            elif end <= res[-1][1]:
                res[-1] = [start, end]

            # otherwise we ignore the interval as its longer and overlapping
            else:
                continue
        
        # the difference is the no. of subtractions
        diff = len(intervals) - len(res)
        return diff