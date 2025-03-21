class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            sm = 0
            for char in list(str(num)):
                sm += int(char)
            num = sm
        return num