class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st += str(len(s)) + "#" + s
        print(st)
        return st

    def decode(self, s: str) -> List[str]:
        i = 0
        final = []
        while i < len(s):
            #read num til #
            start = i
            end = i
            while s[end] != '#':
                end += 1
            l = int(s[start:end]) + 1
            final.append(s[end+1:end+l])
            # i += 1
            i = end+l
        return final
        

