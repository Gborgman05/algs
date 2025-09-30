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
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {}
        least_frequent = None
        for num in nums:
            if num in store:
                store[num] += 1
            else:
                store[num] = 1
        freq_to_val = [[] for _ in range(len(nums) + 1)]
        for key, value in store.items():
            freq_to_val[value].append(key)
        final = []
        # print(freq_to_val)
        for i in range(len(freq_to_val) - 1, -1, -1):
            for n in freq_to_val[i]:
                final.append(n)
                if len(final) == k:
                    return final
        return final


        
