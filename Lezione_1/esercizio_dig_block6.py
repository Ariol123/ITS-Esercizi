
while True:
    numero = int(input("Inserisci numero:"))
    if numero > 0:
        break
fattoriale = 1
i = 1

for i in range(numero):
    fattoriale *=i
    i +=1
print(fattoriale)