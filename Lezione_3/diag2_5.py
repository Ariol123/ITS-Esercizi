n = int(input( "Un numero:"))

if n %1 == 0 and n > 0:
    sum = 0
    i = 1
    while i < n:
        sum = sum + i*i
        i +=1
    print (sum)
else:
    print("Errore n deve essere positivo")





