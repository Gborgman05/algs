class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        final = []
        for interval in sorted(intervals, key=lambda i: i[0]):
            if final and final[-1][1] >= interval[0]:
                final[-1] = [final[-1][0], max(final[-1][1], interval[1])]
            else:
                final.append(interval)
        return final 
        # final = []
        # while intervals:
        #     curr_interval = intervals.pop()
        #     i = 0
        #     while i < len(intervals):
        #         if ((intervals[i][0] >= curr_interval[0] and intervals[i][0] <= curr_interval[1]) or #left inside
        #             (intervals[i][1] <= curr_interval[1] and intervals[i][1] >= curr_interval[0]) or # right inside
        #             (intervals[i][0] <= curr_interval[0] and intervals[i][1] >= curr_interval[1])): # entirely larger
        #             #entirely smaller is handeld by left, right inside logic
        #             curr_interval = [min(intervals[i][0], curr_interval[0]), max(intervals[i][1], curr_interval[1])]
        #             intervals.pop(i)
        #         else:
        #             i+= 1
        #     j = 0
        #     while j < len(final):
        #         if ((final[j][0] >= curr_interval[0] and final[j][0] <= curr_interval[1]) or #left inside
        #             (final[j][1] <= curr_interval[1] and final[j][1] >= curr_interval[0]) or # right inside
        #             (final[j][0] <= curr_interval[0] and final[j][1] >= curr_interval[1])): # entirely larger
        #             #entirely smaller is handeld by left, right inside logic
        #             curr_interval = [min(final[j][0], curr_interval[0]), max(final[j][1], curr_interval[1])]
        #             final.pop(j)
        #         else:
        #             j += 1
        #     final.append(curr_interval)
        # return final

    class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # idk if its sorted or not
        intervals = sorted(intervals, key=lambda a: a[0])
        output = [intervals[0]]
        for start, end in intervals:
            if start <= output[-1][1]:
                output[-1][1] = max(end, output[-1][1])
            else:
                output.append([start, end])
        return output
        