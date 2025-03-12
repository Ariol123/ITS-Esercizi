n_tutor = 10
attesa = 0

while True:
    studente = input("Inserisci lo Studente:")
    if n_tutor > 0:
        n_tutor -= 1
        print("Tutor assegnato con sucesso:")
    else:
        attesa +=1
        print("Studente in Attesa")
    if n_tutor == 0 and attesa > 50:
        break
