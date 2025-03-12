
max_posti = 100


while True:
    nome_corso = input("Nome corso:")
    opzione = input ("Inserisci Opzione,'iscriviti','annulla','visualizza','elimina','esci':")
    if opzione == "iscriviti":
        if max_posti > 0:
            max_posti -= max_posti
        else:
            print("Non ci sono posti disponibili")
    elif opzione == "anulla":
        if max_posti < 100:
            max_posti +=1
        else:
            print("Tutti i posti sono gia disponibili")
    elif opzione == "visualizza":
        print(max_posti)
        print (100 - max_posti)
    elif opzione == "elimina":
        input("Nome corso:")
    elif opzione == "esci":
        break





    


