class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # why do we cap the max instead of - 1
        mn = 1
        mx = max(piles)

        while mn  < mx:
            mid = (mx + mn) // 2
            
            hours_taken = sum([math.ceil(pile  / mid) for pile in piles])
            if hours_taken > h:
                mn = mid + 1
            else:
                mx = mid

        return mx
        

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return False
        l = 1
        r = max(piles)

        while l < r:
            mid = (l+r) // 2
            eaten = sum([math.ceil(pile / mid) for pile in piles])
            if eaten > h:
                l = mid + 1
            elif eaten <= h:
                r = mid
        return r



        return l