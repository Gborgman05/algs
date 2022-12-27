class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_char = {}
        
        for i in range(5):
            num_to_char[ i + 2] = [chr(j) for j in [ord("a") + i * 3, ord("a") + 1 + i * 3, ord("a") + 2 + i * 3]]
        num_to_char[7] = ["p", "q", "r", "s"]
        num_to_char[8] = ["t", "u", "v"]
        num_to_char[9] = [char for char in "wxyz"]
        print(num_to_char)
        
        res = []
        # print(digits)
        # print([char for char in digits])
        for char in digits:
            cur = num_to_char[int(char)]
            if not res:
                for char in cur:
                    res.append(char)
            else:
                new = []
                for char in cur:
                    for rs in res:
                        new.append(rs + char)
                res = new
        return res