class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        i = 0
        flag = False
        while i < len(self.arr):
            if self.arr[i] > num:
                self.arr.insert(i, num)
                flag = True
                break
            i += 1
        if not flag:
            self.arr.append(num)
        
        
        

    def findMedian(self) -> float:
        avg = len(self.arr) % 2 == 0
        if avg:
            l = self.arr[len(self.arr) // 2]
            r = self.arr[len(self.arr) // 2 -1]
            return (l + r) / 2
        else:
            return self.arr[len(self.arr) // 2]
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()