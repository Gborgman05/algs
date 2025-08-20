class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_store = {}
        for char in s:
            if char in s_store:
                s_store[char] += 1
            else:
                s_store[char] = 1
        for char in t:
            if char in s_store:
                if s_store[char] <= 0:
                    return False
                s_store[char] -= 1
            else:
                return False
        for key in s_store:
            if s_store[key] != 0:
                return False
        return True
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_store = {}
        for char in s:
            if char in s_store:
                s_store[char] += 1
            else:
                s_store[char] = 1
        t_store = {}
        for char in t:
            if char in t_store:
                t_store[char] += 1
            else:
                t_store[char] = 1
        return s_store == t_store