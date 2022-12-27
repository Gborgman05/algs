class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0
        i = 0
        string = str
        while i < len(string) and (string[i] == " " or string[i] == "\t"):
            i += 1
        # print(string[i])
        if i == len(string):
            return 0
        neg = False
        if i == len(string):
            return 0
        if string[i] == "-":
            neg = True
            string = string[i + 1:]
        elif string[i] == "+":
            string = string[i + 1:]
        else:
            string = string[i:]
        j = 0
        while j < len(string) and ord("0") <= ord(string[j]) and ord(string[j]) <= ord("9"):
            j += 1
        string = string[:j]
        factor = j - 1
        tot = 0
        for char in string:
            tot += int(char) * 10 ** factor
            factor -= 1
        if neg:
            tot = -tot
        if tot < -2147483648:
            tot = -2147483648
        if tot > 2147483647:
            tot = 2147483647
        return tot