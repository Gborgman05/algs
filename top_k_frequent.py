class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = Counter(nums)
        ans = []
        for num in store:
            if not ans:
                ans.append((num, store[num]))
            else:
                final_index = -1
                for i in range(len(ans)):
                    if store[num] >= ans[i][1]:
                        final_index = i
                        break
                if final_index==-1:
                    ans.append((num, store[num]))
                else:
                    ans.insert(final_index, (num, store[num]))
        return [s[0] for s in ans[:k]]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        for num in nums:
            if num in store:
                store[num] += 1
            else:
                store[num] = 1
            
        a = [(-i[1],i[0]) for i in store.items()]
        heapq.heapify(a)
        final = []
        for i in range(k):
            final.append(heapq.heappop(a)[1])

        return final
