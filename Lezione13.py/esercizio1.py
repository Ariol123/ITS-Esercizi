

def coundown(n):
    while n:
        print(n)
        n-=1
        print (n)
        n==0
        break
    
    if n < 0:
        print("Error")


coundown(5)

def countdown(n:int) -> None:
# n is positive (n >= 0)
if n >=0 :
# print the countdown, while n>=0
while n:
print(n)
n = n - 1
# n is negative (n < 0)
else:
print("Error! Inserted number is negative!")