class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for num in nums:
            if num in store:
                store[num] += 1
            else:
                store[num] = 1
        total = list(store.items())
        total.sort(key=lambda x:x[1], reverse=True)
        return [i[0] for i in total[:k]]
        