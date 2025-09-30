"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda a: a.start)
        prev = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < prev:
                return False
            else:
                prev = interval.end
        return True
