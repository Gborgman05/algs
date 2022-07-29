class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        checker = {}
        if len(p) > len(s):
            return []

        for char in p:
            if char in checker:
                checker[char] += 1
            else:
                checker[char] = 1
        for i in range(len(p)):
            if s[i] in checker:
                checker[s[i]] -= 1
        for i in range(0, len(s) - len(p)):
            print(checker, "is checker checked" )
            if all([val == 0 for val in checker.values()]):
                indices.append(i)
            if s[i] in checker:
                checker[s[i]] += 1
            # print(checker[s[i + len(p - 1)]])
                
            if s[i + len(p)] in checker:
                checker[s[i + len(p)]] -= 1
        if all([val == 0 for val in checker.values()]):
            indices.append(len(s) - len(p))
            
        return indices         