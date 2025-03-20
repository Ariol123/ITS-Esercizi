def recursiveSumInRange(a:int,b:int) -> int:
    if a > b:
        temp:int = a
        a = b
        b = temp
        sum:int = 0
    while b > a:
        sum = sum + b
        b -= 1
        return int(sum)
    if b == a:
        return (a)
    else:
        return (b + recursiveSumInRange(a, b-1))

    



def recursiveSumInRange(a:int,b:int) -> int:
    if a > b:
        temp:int = a
        a = b
        b = temp
    if b == a:
        return(int(a))
    else:
        return int(b + recursiveSumInRange(a, b - 1))
    
print(recursiveSumInRange(10,5))

