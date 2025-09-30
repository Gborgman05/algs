class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-num for num in nums]
        heapq.heapify(self.nums)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        saved = []
        for i in range(self.k):
            saved.append(heapq.heappop(self.nums))
        for save in saved:
            heapq.heappush(self.nums, save)
        return -saved[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)