"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        tmp = []
        for interval in intervals:
            tmp.append((interval.start, 1))
            tmp.append((interval.end, -1))
        tmp.sort(key=lambda x: (x[0], x[1]))

        max_count = 0
        count = 0
        for _, interval_type in tmp:
            count += interval_type
            max_count = max(max_count, count)

        return max_count

        