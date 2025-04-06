class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = {}

        for st in strs:
            new = ''.join(sorted(st))
            if new in final:
                final[new].append(st)
            else:
                final[new] = [st]
        return list(final.values())
                    

        