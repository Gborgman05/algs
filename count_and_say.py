class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.RLE(self.countAndSay(n-1))
    def RLE(self, s: str) -> str:
        """
        Encode a string with Run-Length Encoding
        """
        final_str = ""
        cur_letter = ""
        count = 0
        for i in range(len(s)):
            if cur_letter == "": 
                cur_letter = s[i]
                count = 1
            elif cur_letter != s[i]: # changed letter
                final_str += str(count) + cur_letter 
                cur_letter = s[i]
                count = 1
            else: # continue letter
                count += 1
                
        if count > 0:
            final_str += str(count) + cur_letter 
        return final_str