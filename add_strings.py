class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sm = []
        place = 1
        carry = False
        while place <= len(num1) or place <= len(num2):
            curr = 0
            if len(num1) > place - 1:
                curr += int(num1[-place]) #* 10 ** (place - 1) 
            if len(num2) > place - 1:
                curr += int(num2[-place]) #* 10 ** (place - 1) 
            if carry:
                curr += 1 
                carry = False
            if curr >= 10:
                curr -= 10
                carry = True
            sm.append(str(curr))
            place += 1
        if carry:
            sm.append("1")
        return "".join( reversed(sm))
