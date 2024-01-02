def minion_game(string):
    # your code goes here
    string = string.upper()
    vowels = "AEIOU"
    store = {}
    v = 0
    c = 0
    res = [string[i: j] for i in range(len(string))
          for j in range(i + 1, len(string) + 1)]
    for substr in res:
        if substr[0] in vowels:
            v += 1
        else:
            c += 1
    # for char in string:
    #     print(char)
    #     if char in store: 
    #         pass
    #     elif char in vowels:
    #         store[char] = True
    #         v += 1
    #     else:
    #         store[char] = False
    #         c += 1
    # print(v)
    # print(c)
    if v == c:
        print("Draw")
    elif v > c:
        print("Kevin " + str(v))
    else: 
        print("Stuart " + str(c))
        

if __name__ == '__main__':
    s = input()
    minion_game(s)
