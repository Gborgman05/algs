class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        first = True
        if x < 0:
            neg = True
            x = -x
        fin = 0
        pw = 1
        while x > 0:
            cmp = x % 10 ** pw
            if cmp > 0:
                tmp = cmp
                x -= cmp
                fin *= 10
                fin += cmp // 10 ** (pw -1)
            else:
                fin *= 10
            pw += 1
        if neg:
            fin = -fin
        if fin > 2 ** 31 - 1 or fin < -1 * 2 ** 31:
            return 0
        return fin