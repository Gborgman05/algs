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

            

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_point = [((point[0] ** 2 + point[1] ** 2) ** 0.5, point) for point in points]
        heapq.heapify(dist_point)
        final = []
        for i in range(k):
            final.append(heapq.heappop(dist_point)[1])
        return final


        