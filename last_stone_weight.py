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

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            res = a - b 
            if res != 0:
                heapq.heappush(stones, res)
        if not stones:
            return 0
        return -stones[0]

        
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            c = a - b
            if c:
                heapq.heappush(stones, c)
        if not stones:
            return 0
        return -stones[0]