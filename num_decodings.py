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

class Solution:
    def numDecodings(self, s: str) -> int:
        # 1234567
        # 1 2 3 4 5 6 7
        # 12 3 4 5 6 7
        # 1 23
        if s[0] == '0' or s[-1] == '0' and int(s[-2]) > 2:
            return 0
        ways = [0] * len(s)
        for i in range(len(ways)):
            if i > 0:
                if int(s[i-1]) < 3 and int(s[i-1]) > 0 and int(s[i]) < 7:
                    ways[i] = ways[i-1] + 1
                else:
                    ways[i] = ways[i-1]            
            else:
                ways[i] = 1
        return ways[-1]
        