# very slow, should use sorting of string characters to optimize
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        store = []
        for st in strs:
            cnt = {}
            for char in st:
                if char in cnt:
                    cnt[char] += 1
                else:
                    cnt[char] = 1
            inserted = False
            for i in range(len(store)):
                if cnt == store[i]:
                    final[i].append(st)
                    inserted = True
            if not inserted:
                final.append([st])
                store.append(cnt)
        return final
        