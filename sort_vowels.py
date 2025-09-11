class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        vowels = list("aeiou")
        found_vowels = sorted([a for a in s if a.lower() in vowels])
        j = 0
        for i in range(len(s)):
            if s[i].lower() in vowels:
                s[i] = found_vowels[j]       
                j += 1
        return "".join(s)