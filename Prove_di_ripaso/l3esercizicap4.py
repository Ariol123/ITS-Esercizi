'''
Esercizio 4
Scrivere un programma che consenta all'utente di inserire una sequenza di numeri reali non negativi (sia interi che decimali). L'inserimento termina quando viene fornito un numero negativo, che funge da sentinella e non deve essere considerato nei calcoli.

Il programma deve:

Calcolare la media dei soli numeri interi inseriti. Utilizzate la funzione is_integer() per verificare se il numero inserito è un intero.
Determinare e visualizzare il numero più grande e il numero più piccolo tra tutti quelli inseriti (sia interi che decimali).


'''

numeri: int|float = float(input("Scrivi nr, se negativo esce: "))
media_int = 0
count = 0
min =99999
max =0

while numeri >0:

    if numeri.is_integer():
        media_int += numeri
        count +=1
        media_int = media_int / count
    if min > numeri:
        min = numeri
    if max < numeri:
        max = numeri
    numeri: int|float = float(input("Scrivi nr, se negativo esce: "))
print(min,"\n", max,"\n",media_int )


