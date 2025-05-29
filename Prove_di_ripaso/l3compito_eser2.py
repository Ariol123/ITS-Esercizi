'''
Esercizio 2
Scrivere un programma che acquisisca una stringa inserita dall'utente e calcoli il numero totale di spazi presenti nella stringa. Il risultato deve essere visualizzato in output.

'''

sting = input("Parola con spazi")

caunt = 0


while len(sting) > caunt:
    
    for i in sting:
        if i == " ":
            caunt +=1
    print(caunt)
    break