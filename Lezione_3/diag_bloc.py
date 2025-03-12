



max_posti = int(input("Inserisci in nr max:"))
                  
liberi:int = max_posti

while True:
    opzione = input("inserisci opzione, ingresso, uscita, stato esci:").lower()

    if opzione == "ingresso":
        if liberi > 0:
            liberi -=1
        else:
            print("non ci sono posti liberi")

    elif opzione == "uscita":
        if liberi < max_posti:
            liberi +=1
        else:
            print("tutti i posti sono disponibili")

    elif opzione == "stato":
        print (f"Posti{liberi}")
        print (max_posti - liberi)
    elif opzione == "esci":
        break
    else:
        print("errore")


        
    



    
    

