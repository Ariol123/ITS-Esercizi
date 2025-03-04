

numero:int= int(input("Inserisci nr:"))

if numero < 2:
    print("Nr non primo")
else:
    div = 2
    while div < numero:
        if numero%div!=0:
            div +=1
        

if numero >2 and numero/2 :
    numero_div=numero/2
    if numero_div>numero:
        numero%numero_div==0
    print("Nr non Primo.")

