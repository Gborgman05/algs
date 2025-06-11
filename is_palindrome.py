class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s )// 2):
            if s[i] != s[-i -1]:
                return False
        return True
    
    # with alphanumeric scanning mod
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            print(start, " ", end)
            while not s[start].isalnum() and start < end:
                start += 1
            while not s[end].isalnum() and end > start:
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()
        while l < len(s) and not((ord(s[l]) <= ord("z") and ord(s[l]) >= ord("a")) or (ord(s[l]) <= ord("9") and ord(s[l]) >= ord("0"))):
            l += 1
        while r >= 0 and not((ord(s[r]) <= ord("z") and ord(s[r]) >= ord("a")) or (ord(s[r]) <= ord("9") and ord(s[r]) >= ord("0"))):
            r -= 1
        
        while l < r:
            while l < len(s) and not((ord(s[l]) <= ord("z") and ord(s[l]) >= ord("a")) or (ord(s[l]) <= ord("9") and ord(s[l]) >= ord("0"))):
                l += 1
            while r >= 0 and not((ord(s[r]) <= ord("z") and ord(s[r]) >= ord("a")) or (ord(s[r]) <= ord("9") and ord(s[r]) >= ord("0"))):
                r -= 1
            # print(l)
            # print(r)
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True