
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

