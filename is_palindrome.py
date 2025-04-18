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
