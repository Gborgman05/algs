class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        overlapping = {i: 0 for i in range(len(intervals))}
        dep_map = {i: [] for i in range(len(intervals))}
        dep_map_len = 0
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                # double counting the second here
                if intervals[i][1] > intervals[j][0] and intervals[j][1] >= intervals[i][0]:
                    #overlapping
                    overlapping[i] += 1
                    overlapping[j] += 1
                    dep_map[i].append(j)
                    dep_map[j].append(i)
                    dep_map_len += 2
        #get the ones with biggest overlapping
        ordered = sorted(overlapping.items(), key=lambda item: item[1], reverse=True)
        i = 0
        while dep_map_len > 0:
            for j in dep_map[ordered[i][0]]:
                dep_map[j].remove(ordered[i][0])
                dep_map_len -= 2
            i += 1
        print(dep_map)
        return i
