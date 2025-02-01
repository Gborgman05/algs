class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for row in range(numRows)]
        direction = False
        index = 0 
        if numRows < 2:
            return s
        for char in s:
            rows[index].append(char)
            if index == numRows - 1:
                direction = not direction
            if index == 0:
                direction = not direction
            if direction:
                index += 1
            elif not direction:
                index -= 1
        return "".join(["".join(row) for row in rows])
