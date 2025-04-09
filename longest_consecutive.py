class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
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
                    back -= 1
                    already_seen[back] = 1
            print(forward, " ", num, " ", back)
            forward = back
            if num not in already_seen:
                already_seen[num] = 1
            while forward+1 in store:
                already_seen[forward+1] = already_seen[forward] + 1
                forward += 1
        return max(already_seen.values())
        