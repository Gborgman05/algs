class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_to_point = {}
        dists = []
        for point in points:
            dist = (point[0] ** 2 + point[1] ** 2) ** 0.5
            dists.append((dist, point[0], point[1]))
        heapq.heapify(dists)
        res = []
        while k > 0:
            tmp = heapq.heappop(dists)
            res.append((tmp[1], tmp[2]))
            k -= 1
        return res

            

        