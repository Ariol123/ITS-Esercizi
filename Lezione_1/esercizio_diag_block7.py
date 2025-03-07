

pari = 0
dispari = 0
cont = 0

while True:
    numero = input("Inserisci N:")
    if numero %2 ==0:
        pari +=1
    else:
        dispari +=1
    cont +=1
    if cont == 10:
        break
print(pari)
print(dispari)

