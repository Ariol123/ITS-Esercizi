'''
Esercizio 3C-00A. Scrivere un programma in Python che richieda all'utente di inserire un numero intero rappresentante il numero di neonati e utilizzi lo statement match per fornire una risposta appropriata:

- Se il numero inserito è 1, stampare "Congratulazioni!"
- Se il numero inserito è 2, stampare "Wow! Gemelli!"
- Se il numero inserito è 3, stampare "Wow! Tre!"
- Se il numero inserito è 4, stampare "Mamma mia Quattro! Wow!"
- Se il numero inserito è 5, stampare "Incredibile! Cinque!"
- Altrimenti, stampare "Non ci credo! n bambini!", sostituendo n con il numero inserito.

Expected Output:

Inserire il numero di neonati: 2
Wow! Gemelli!

- - - - - - - - - - - - - - - - - -

Inserire il numero di neonati: 5
Incredibile! Cinque!

- - - - - - - - - - - - - - - - - -

Inserire il numero di neonati: 7
Non ci credo! 7 bambini!
'''

neonati:int = int(input("inserisci un numero intero rappresentanta il numero di neonati"))

match neonati:

    case 1:
        print("Congratulazioni!")
    case 2:
        print("Wow! Gemelli!")
    case 3:
        print("Wow tre")
    case _:
        print(f"Non ci credo! {neonati} bambini!")


