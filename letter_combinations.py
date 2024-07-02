class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []
        num_to_letter = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        for key in num_to_letter:
            num_to_letter[key] = list(num_to_letter[key])
        final = [""] #num_to_letter[digits[0]]
        #digits = digits[1:]
        for letter in digits:
            # print(final)
            # print(digits)
            permute = []
            for new in num_to_letter[letter]:
                for old in final:
                    permute.append(old + new)
            final = permute
        return final