'''
Esercizio 1
Scrivere un programma che permetta all'utente di inserire una serie di parole in input, terminando l'inserimento quando viene digitata la parola "fine" (che non deve essere considerata nell'elaborazione).
Per ogni parola inserita, il programma deve verificare se il primo e l'ultimo carattere sono uguali e visualizzare un messaggio corrispondente.



'''

while True:
    words = input("Parole:")


    if words == "fine":
        break
    i = 0
    while i < len(words):
        prima = words[0]
        ultima = words[-1]
        i +=1
    if prima == ultima:
        print("Daje")

        

