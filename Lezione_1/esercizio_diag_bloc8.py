


soglia= int(input("Inserisci un Valore:"))

cont =0


while True:
    numero = input("inserisci un Numero:")
    if numero > soglia:
        print(numero)
    cont +=1
    if cont==7:
        break
