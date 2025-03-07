
nome = input("inserisci Nome:")
vendite = int(input("Numero di vendite:"))
max = vendite
min_nome = nome
min:int = vendite
cont = 0
while True:
    nome_1= input("inserisci Nome:")
    vendite_1=int(input("Numero di vendite:"))
    if vendite_1 > max:
       max = vendite_1
       max = nome_1
    else:
        
        if vendite_1 < min:
            min_nome = nome_1
            min = nome_1

    cont+=1
    if cont ==19:
        break
      
      
      
print(min)
print(max)
print(f"{nome}\n{vendite}\n{min}\n{max}")



