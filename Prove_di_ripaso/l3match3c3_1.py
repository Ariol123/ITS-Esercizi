'''
Esercizio 3C-3. Creare in Python una lista vuota chiamata 'oggetti'. Con un ciclo, riempire questa lista con tre oggetti diversi.
Scrivere, poi, un programma che utilizzi un match statement per classificare gli oggetti presenti nella lista:

- ["penna", "matita", "quaderno"] → "Materiale scolastico"
- ["pane", "latte", "uova"] → "Prodotti alimentari"
- ["sedia", "tavolo", "armadio"] → "Mobili"
- ["telefono", "computer", "tablet"] → "Dispositivi elettronici"
- Qualsiasi altra lista → "Categoria sconosciuta"

Expected Output:

['casa', 'hotel', 'b&b']
Categoria sconosciuta

--------------------------

['penna', 'matita', 'quaderno']
Materiale scolastico
 
'''

oggetti:list =[]


while True:
    temp = input("Inserire un oggetto tipo penna,matita:")
    oggetti.append(temp)
    if len(oggetti) == 3:
        break
    print(oggetti)

match oggetti:

    case ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    case ["pane", "latte","uova"]:
        print("Bella ciaao")
    case _:
        print ("time out")