class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = "aeiou"
        vowel_count = 0
        for char in s:
            if char.lower() in vowels:
                vowel_count += 1
        
        if vowel_count == 0:
            return False
        if vowel_count % 2 == 1:
            return True
        else:
            return True
        # if its empty, alice loses, 
        # if count is odd, alice takes whole string in first turn
        # if count is even, then alice can take whole string except 1 vowel, which causes enemy to lose