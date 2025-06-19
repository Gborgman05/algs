class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-val for val in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            heavy = heapq.heappop(stones)
            light = heapq.heappop(stones)
            if heavy != light:
                heapq.heappush(stones, heavy - light)
        if not stones:
            return 0
        return -stones[0]
