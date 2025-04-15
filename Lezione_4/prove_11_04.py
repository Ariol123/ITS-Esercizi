'''sum = 0
for interation in range(1,11):
    sum += interation
print(sum)'''

#Stessa cosa
#--------------------------------------------
def sommNumeri(a:int,b:int):
    sum:int = 0
    for interation in range(a + b+1):
        sum = sum + interation
    return sum


sommNumeri(1, 10)

