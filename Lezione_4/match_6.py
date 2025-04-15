
'''Esercizio 3C-4. Scrivere un programma in Python che permetta all'utente di inserire il nome di un animale e, utilizzando un match statement,
 identifichi a quale categoria esso appartiene. L'animale deve essere classificato in una delle seguenti categorie:

- Mammiferi: cane, gatto, cavallo, elefante, leone.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco.
- Pesci: squalo, trota, salmone, carpa.

Se l'animale non appartiene a nessuna delle categorie sopra elencate,  mostrare un messaggio indicante che il programma non è in grado di classificare 
l'animale inserito.

Suggerimento: Utilizzare una lista per ognuna della quattro categorie.

Expected Output:

Digita il nome di un animale: cane
Output: cane appartiene alla categoria dei Mammiferi!

- - - - - - - - - - - - - - - - - - - - - - - - - - - -

Digita il nome di un animale: coccodrillo
Output: coccodrillo appartiene alla categoria dei Rettili!

'''
animal: str = input("Scrivere il nome di un animale:"),input("habitat")



mammiferi:list =  ["cane", "gatto", "cavallo", "elefante", "leone"]
rettili:list = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli:list = ["aquila", "pappagallo", "gufo", "falco"]
pesci:list= ["squalo", "trota", "salmone", "carpa"]

terra = {"animali":["cane","gatto","cavallo"]}



match animal:
    case animal if animal in mammiferi:
        print("Mammiferi")
    case animal if animal in rettili:
        print("E un Rettile.")
    case animal if animal in uccelli:
        print("Questo e un Volatile")
    case animal if animal in pesci:
        print("e un pesce")
    case _:
        print("l programma non è in grado di classificare l'animale inserito.")