class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        offset = 1
        fin = ""
        while offset <= len(a) and offset <= len(b):
            val = int(a[-offset]) + int(b[-offset]) + carry
            if val <= 1:
                fin = str(val) + fin
            carry = 0
            if val == 2:
                carry = 1
                fin = "0" + fin
            if val == 3:
                carry = 1
                fin = "1" + fin
            offset += 1
        while offset <= len(a):
            val = int(a[-offset]) + carry
            carry = 0
            if val <= 1:
                fin = str(val) + fin
            if val == 2:
                carry = 1
                fin = "0" + fin    
            offset += 1
        while offset <= len(b):
            val = int(b[-offset]) + carry
            carry = 0
            if val <= 1:
                fin = str(val) + fin
            if val == 2:
                carry = 1
                fin = "0" + fin     
            offset += 1
        if carry:
            fin = "1" + fin
        return fin
            