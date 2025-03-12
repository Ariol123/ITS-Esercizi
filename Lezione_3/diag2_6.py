x = int(input("Inserisci x:"))
sum = 0
if x > 0:
    i = 0
    for i in range(10):
        n = int(input("Inserisci n:"))
        if x%2==0:
            if n > x / 2:
                sum += n
        elif n < x:
            sum = sum + n
        i += 1
    print(sum)
else:
    print("Errore x deve esere positivo")
            



