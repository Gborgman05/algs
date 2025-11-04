class Solution:
    def reverseVowels(self, s: str) -> str:
        a = list(s)
        print(a)
        saved = []
        for char in a:
            if char.lower() in "aeiou":
                saved.append(char)
        
        for i in range(len(a)) :
            if a[i].lower() in "aeiou":
                a[i] = saved.pop()
        return "".join(a)
