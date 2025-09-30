class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        def merge(interval1, interval2):
            return [min(interval1[0], interval2[0]), max(interval2[1], interval1[1])]
        while i < len(intervals):
            interval = intervals[i]
            if (newInterval[0] <= interval[1] and newInterval[0] >=interval[0]) or (newInterval[1] >= interval[0] and newInterval[1] <= interval[1]) or (newInterval[0] <= interval[0] and newInterval[1] >= interval[1]) : # don't need anything from before this
                newInterval = merge(newInterval, intervals.pop(i))
            else:
                i += 1
        intervals.append(newInterval)
        return sorted(intervals)

        
            

