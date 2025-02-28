'''
Esercizio 3C-10. Scrivere un programma in Python che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica), 
salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data."

Expected Output:

Inserisci il giorno: 25
Inserisci il mese: 12
Output: Il 25/12 è Natale!

- - - - - - - - - - - - - - -

Inserisci il giorno: 5
Inserisci il mese: 3
Output: Nessuna festività importante in questa data.

'''
 
giorno: int = int (input ("inserisci giorno"))
mese: int = int(input("inserisci mese"))
festività :tuple= (giorno,mese)
match festività:
    case (1,1):
        print("Capodanno")
    case (14,2):
        print("San Valentino")
    case (15,8):
        print("Ferragosto")
    case (31,10):
        print("Halloween")
    case (25,10):
        print("Natale")
    case _:
        print("Nessuna festività importante in questa data.")

