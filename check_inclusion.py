class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        store = {}
        for char in s1:
            if char in store:
                store[char] += 1
            else:
                store[char] = 1
        
        total_taken = len(s1)
        check = {}
        for i in range(len(s2)):
            if s2[i] not in store:
                check = {}
                total_taken = len(s1)
            else:
                if s2[i] in check:
                    check[s2[i]] += 1
                else:
                    check[s2[i]] = 1
                total_taken -= 1
                if total_taken < 0:
                    check[s2[i-len(s1)]] -= 1
                    total_taken += 1
            if check == store:
                return True
        return False