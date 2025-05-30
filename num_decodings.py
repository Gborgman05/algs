class Solution:
    def numDecodings(self, s: str) -> int:
        final = [0] * (len(s) + 1)
        if s[0] == '0':
            return 0


        for i in range(len(s) + 1):
            if i <= 1:
                final[i] = 1
            else:
               # print(int(s[i-2:i]))
                if  int(s[i-2:i]) > 9 and int(s[i-2:i]) < 27:
                    final[i] = final[i-2]
                if  int(s[i-1:i]) < 10 and int(s[i-1]) > 0:
                    final[i] += final[i-1]
       # print(final)

        return final[-1]