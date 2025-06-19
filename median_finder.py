class MedianFinder:

    def __init__(self):
        self.heap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)
        

    def findMedian(self) -> float:
        if len(self.heap) % 2 == 0:
            #find average from two
            index = len(self.heap) // 2 - 1
            replace = []
            for i in range(index):
                replace.append(heapq.heappop(self.heap))
            if len(self.heap) < 1:
                return None
            else:
                # print(self.heap)
                res = self.heap[0]
                tmp = heapq.heappop(self.heap)
                replace.append(tmp)
                # print(res, " ", tmp)
                res = (res + self.heap[0]) / 2
                for num in replace:
                    heapq.heappush(self.heap, num)

                return res
        else:
            index = len(self.heap) // 2
            replace = []
            for i in range(index):
                replace.append(heapq.heappop(self.heap))
            ans = self.heap[0]
            for num in replace:
                heapq.heappush(self.heap, num)
            return ans

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()