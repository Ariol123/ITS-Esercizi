
max= float(input(f"inserisci nr:"))
cont=1


while  cont< 4:
    cont+=1
    number= float(input(f"inserisci nr:"))
    number>max
    max=number

print(max)



while True:
    n = float(input("Inserisci un nr:"))
    if n > max:
        max = n
    cont +=1
    if cont ==4:
        break


for i in range(3):
    n = float(input("inserisci nr:"))
    if n > max:
        max =n
    print("In max{n}")


max = int(input("Max:"))

cont = 1






while cont< 4:
    cont +=1
    numero = int(input("numero"))
if numero > max:
    max = numero
print(max)



max = int(input("Max:"))
cont = 1




while True:
    cont += 1
    number = int(input("Numero:"))
    if numero > max:
        max = numero
    if cont ==4:
        break
print(max)


max = int(input("Max:"))
i = 0
for i in range(3):
    i +=1
    numero = int(input("numero"))
    if numero > max:
        max = numero
print(max)

