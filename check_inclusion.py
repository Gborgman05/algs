# can speed this up by using only one dictionary setting counts to negative from first string
#O(n)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1store = {}
        for char in s1:
            if char in s1store:
                s1store[char] += 1
            else:
                s1store[char] = 1
        if len(s2) < len(s1):
            return False
        s2_store = {}
        for i in range(len(s1)):
            if s2[i] in s2_store:
                s2_store[s2[i]] += 1
            else:
                s2_store[s2[i]] = 1
        if s1store == s2_store:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            if s2[r] in s2_store:
                s2_store[s2[r]] += 1
                if s2_store[s2[r]] == 0:
                    del s2_store[s2[r]]
            else:
                s2_store[s2[r]] = 1
            if s2[l] in s2_store:
                s2_store[s2[l]] -= 1
                if s2_store[s2[l]] == 0:
                    del s2_store[s2[l]]
            else:
                s2_store[s2[l]] = -1
            if s1store == s2_store:
                return True
            l += 1
        if s1store == s2_store:
            return True
        else:
            return False
        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        store = {}
        for char in s1:
            if char in store:
                store[char] += 1
            else:
                store[char] = 1
        start, end = 0, 0
        test = {}
        test_count = 0
        store_count = len(s1)
        while end < len(s2):
            # print(start)
            # print(end)
            # print(test)
            if store == test:
                return True

            while end < len(s2) and len(s1) > test_count:
                if s2[end] not in test:
                    test[s2[end]] = 1
                    test_count += 1
                else:
                    test[s2[end]] += 1
                    test_count += 1
                end += 1
            if test == store:
                return True
            
            test[s2[start]] -= 1
            if test[s2[start]] == 0:
                del test[s2[start]]
            start += 1
            test_count -= 1
        return False
