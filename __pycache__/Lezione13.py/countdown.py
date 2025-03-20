def countdown(n:int)-> None:
    if n < 0:
        print("Error! Inserted number is negative")
    elif n == 0:
        print(0)
    else:
        print(n)
        countdown(n-1)

countdown(5)


def sum(n:int) -> int:
    if n < 0 :
        print("Error")
        return None
    else:
        sum = 0
    while n:
        
        sum:int= sum + n
        n-=1
    return int(sum)

#print(sum(5))


def recursiveSum(n:int) -> int:
# n is negative
    if n < 0:
        print("Errore! ")
        return None
    elif n == 0:
        return 0
    else:
        return int(n + recursiveSum(n-1))
    
print(recursiveSum(5))


def recursiveSumInRange(a:int,b:int) -> int:
    if a > b:
        while range(a,b):

            sum += range(a,b)
            return(sum)
    

    
print(recursiveSumInRange(5,10))