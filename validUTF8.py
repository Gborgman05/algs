# adapted from valid UTF8oneStr because I didn't understand the encoding could be multiple sets of up to 4 bytes
# however code is difficult to read due to adaptation
# basic idea is to read the number of leading bits, check the corresponding 1-4 bytes, then delete them
# start again in a loop.
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        if len(data) == 1:
            return data[0] < 128
        while len(data) > 0:
            checker = 0
            pos = 7
            while pos >= 0:
                if data[0] < checker + 2 ** pos:
                    break
                checker += 2 ** pos
                pos -= 1
            leading = 7 - pos
            print(leading)
            if leading == 0:
                if data[0] < 128:
                    data.pop(0)
                    continue
                else:
                    return False
            if leading > 4:
                return False
            if leading == 1:
                return False
            if len(data) < leading:
                return False
            if data[0] < checker:
                return False
            checker += 2 ** pos
            if data[0] >= checker:
                print("a")
                return False
            for i in range(1, leading):
                if data[i] < 128:
                    print("b")
                    print(data[i])
                    return False
                if data[i] >= (128 + 64):
                    print("c")
                    return False
            for i in range(leading):
                data.pop(0)
        return True
            
        
        