class Solution:
    def partition(self, s: str) -> List[List[str]]:
        final = []
        def is_palindrome(a):
            for i in range(len(a) // 2):
                if a[i] != a[-i-1]:
                    return False
            return True
        def backtrack(s, curr, cut):
            if not s:
                final.append(curr[:])
                return
            if cut > len(s): 
                return
            pre = s[:cut]
            if is_palindrome(pre):
                curr.append(pre)
                backtrack(s[cut:], curr, 1)
                curr.pop()
            
            backtrack(s, curr, cut + 1)
        
        
        backtrack(s, [], 1)

        return final