class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_num = None


        maxes = []
        for i in range(0, len(nums) - k + 1):
            if max_num is None or nums[i-1] == max_num:
                max_num = max(nums[i:i + k])
            else:
                max_num = max(max_num, nums[i + k - 1])
            maxes.append(max_num)
        return maxes
    #works for cases except k is large

    class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_num = None
        q = deque()


        maxes = []
        for i, num in enumerate(nums):
            while q and q[-1] < num:
                q.pop()
            q.append(num)

            if i >= k and nums[i-k] == q[0]:
                q.popleft()
            if i >= k - 1:
                maxes.append(q[0])
            
        return maxes
