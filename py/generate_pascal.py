class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        total = []
        cur = [1]
        total.append(cur)
        while len(total) < numRows:
            new = [1]
            i = 0
            for i in range(len(cur)):
                tot = cur[i]
                if i + 1 < len(cur):
                    tot += cur[i+1]
                new.append(tot)
            cur = new
            total.append(cur)
        return total