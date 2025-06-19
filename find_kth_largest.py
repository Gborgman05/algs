class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        larger = [x for x in nums if x > pivot]
        same = [x for x in nums if x == pivot]
        smaller = [x for x in nums if x < pivot]
        
        if len(larger) >= k:
            return self.findKthLargest(larger, k)
        elif k > len(larger) + len(same):
            return self.findKthLargest(smaller, k - len(larger) - len(same))
        else:
            return pivot


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        while k > 1:
            k -= 1
            heapq.heappop(nums)
        return -nums[0]