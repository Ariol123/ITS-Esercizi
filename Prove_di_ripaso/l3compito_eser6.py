'''
Esercizio 6
Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.
Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque il prodotto correttamente.
'''

a = int(input("Numero a :"))

b = int(input("Numero b :"))


prod = 1
while True:
    if a >= b:
        prod *= a
        a +=1
        if a > b:
            break
    if a <= b:
        prod *= a
        a +=1
        if a > b:
            break
print (prod)
    