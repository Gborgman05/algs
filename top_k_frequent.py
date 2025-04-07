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