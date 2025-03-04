myList:list[int,...] = [1,2,3,4,5]
print(myList)
print(*myList)


def add(*args):
    num = 0
    for number in args:
        num+=num
    return num
    
print(add(4,7))
