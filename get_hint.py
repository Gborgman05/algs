class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        b = 0
        cnts = {}
        for char in secret:
            if char in cnts:
                cnts[char] += 1
            else:
                cnts[char] = 1
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
                cnts[secret[i]] -= 1
        for i in range(len(secret)):
            if secret[i] != guess[i] and guess[i] in cnts and cnts[guess[i]] > 0:
                b += 1
                cnts[guess[i]] -= 1
        return f'{a}A{b}B'
            
                