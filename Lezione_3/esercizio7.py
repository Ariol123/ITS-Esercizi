cont = 0
sum = 0

while True:
    scelta = input("Inserisci scelta, si,no:").lower()
    if scelta  == "si":
        voto = int(input("Voto"))
        while True:
            if voto > 0:
                break
        
            
            else:
                print("Errore")
        cont +=1
        sum = sum + voto
    elif scelta =="no":
        if cont > 0:
            media = sum/cont
            print(media)
        else:
            print("Nessun voto inserito")
        break