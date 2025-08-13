class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda a: a[0])
        final = {}
        i = 0
        heap = []
        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                interval = intervals[i]
                heapq.heappush(heap, (interval[1]-interval[0], interval[1]))
                i += 1
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            if heap:
                # print(heap)
                tmp = heap[0][0]
                # print(tmp)
                final[query] = tmp + 1
            else:
                final[query] = -1
        return [final[q] for q in queries]