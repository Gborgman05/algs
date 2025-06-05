class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        store = {}
        for card in hand:
            if card in store:
                store[card] += 1
            else:
                store[card] = 1
        while store:
            start = min(store.keys())
            remaining = groupSize
            while remaining > 0:
                if start not in store or store[start] < 1:
                    return False
                store[start] -= 1
                if store[start] < 1:
                    del store[start]
                start += 1
                remaining -= 1
        return True

            
