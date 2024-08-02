def solve(s):
    cap = True
    new = ""
    for i in s:
        if cap:
            if ord(i) <= ord('z') and ord(i) >= ord('a'):
                new += chr(ord(i) - 32)
            else:
                new += i
            cap = False
            continue
        if i == ' ':
            cap = True
        new += i
    return new