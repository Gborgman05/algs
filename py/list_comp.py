# totally unintended use of dictionaries in list comprehension problems
if __name__ == '__main__':
    mydict = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score not in mydict:
            mydict[score] = [name]
        else:
            mydict[score] = mydict[score] + [name]
    names = sorted(mydict[sorted(list(mydict.keys()))[1]])
    for name in names:
        print(name)
    
        
    # print(mylist)