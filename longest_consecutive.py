class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = {}
        for num in nums:
            store[num] = 1
        already_seen = {}
        for num in store:
            back, forward = num, num
            while back-1 in store:
                if back-1 in already_seen:
                    already_seen[back] = already_seen[back-1] + 1
                    break
                else:
                    already_seen[back] = 1
                    back -= 1
                
            while forward+1 in store:
                if forward+1 in already_seen:
                    already_seen[]

            else:
                store[num] = 1
        return max(store.values())
        