# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # find the first and the last index of each character
        # if that character's start falls between another letters start and end it must be included in that
        store = {}
        for i in range(len(s)):
            if s[i] in store:
                store[s[i]][1] = i
            else:
                store[s[i]] = [i, i]
        print (store.items())
        final = []
        for char, start_stop in store.items():
            final = self.combine(final, start_stop)
        return final
        
    def combine(self, intervals, new_interval):
        i = 0
        while i < len(intervals):
            if new_interval[0] < intervals[i][1] and new_interval[0] > intervals[i][0] or new_interval[1] < intervals[i][1] and new_interval[1] > intervals[i][0]:
                new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]
                intervals.pop(i)
            else:
                i += 1
            intervals.append(new_interval)
        return intervals
