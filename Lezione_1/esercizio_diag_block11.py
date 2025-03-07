liberi = 20


while True:
    opzioni_poss = input("Insserire opzioni; Prenota o libera, esci:").lower()
    if opzioni_poss == "prenota":
        if liberi > 0:
            liberi -=1
        if liberi <=0:
            print("Non ci sono posti liberi")

    elif opzioni_poss == "libera":
            if liberi < 20:
                liberi +=1
            if liberi ==20:
                print("Tutti i posti sono liberi")
    elif opzioni_poss == "visualizza":
         print(liberi)
         print (20-liberi)
    elif opzioni_poss == "esci":
         break
    



