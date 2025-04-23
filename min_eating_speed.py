class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 0
        sm = 0
        mx = max(piles)
        mn = 1
        while mn < mx:
            speed = (mx + mn) / 2
            sm = sum((x + speed - 1) / speed for x in piles)
            if sm > h:
                mn = speed + 1 
            else:
                mx = speed
        
        return speed