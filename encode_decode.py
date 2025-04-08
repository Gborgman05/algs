class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        first = True
        for st in strs:
            if first:
                first = False
                final += str(len(st))
            else:
                final += " " + str(len(st)) 
        final += '#'
        for st in strs:
            final += st
        return final

    def decode(self, s: str) -> List[str]:
        split_index = s.index('#')
        if split_index == 0:
            return []
        counts = s[:split_index]
        string = s[split_index + 1:]
        counts = [int(t) for t in counts.split(" ")]
        final = []
        i = 0
        for count in counts:
            final.append(string[i:i+count])
            i += count
        return final
        