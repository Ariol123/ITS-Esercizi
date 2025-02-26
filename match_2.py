
'''


nome = str(input("Inserisci nome:"))

genere = str(input("inserisci genere:")).lower()
match genere:
    case "m":
        print(f"{nome}\nMaschio")
    
    case "f":
        print(f"{nome}\nFemina")
    case _:
        print(f"Mi di spiace {nome} genere non valido")

'''


