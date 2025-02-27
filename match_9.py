'''
Si scriva un programma in python che computi la statistica di otto lanci di una moneta.
Per ciascuno dei lanci effettuati, l'utente inserisce "t" o "T" se è uscito "testa", mentre inserisce "c" o "C" se è uscito "croce".
Il programma deve mostrare in output il numero totale e la percentuale dei risultati "testa" e "croce".

'''

lancio_moneta = 0
testa = 0
croce = 0
risultato:str =str(input("Inserisci t  T per testa o c C Croce:")).lower()
while lancio_moneta < 8:
    match risultato:
        case "t":
            lancio_moneta += 1
            testa +=1
        case "c":
            
            croce +=1
            lancio_moneta += 1
        case _:
            print("strunz")
    risultato:str =str(input("Inserisci t  T per testa o c C Croce:")).lower()

testa: float = (testa / 8) * 100
croce: float = (croce / 8) * 100

print(testa)
print(croce)