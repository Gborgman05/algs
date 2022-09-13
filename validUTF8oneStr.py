class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        if len(data) == 1:
            return data[0] < 128
        leading = len(data)
        checker = 0
        pos = 7
        for i in range(leading):
            checker += 2 ** pos
            pos -= 1
        print(checker)
        if data[0] < checker:
            return False
        checker += 2 ** pos
        if data[0] >= checker:
            return False
        for i in range(1, len(data)):
            if data[i] < 128:
                return False
            if data >= (128 + 64):
                return False
        return True
            
        
        