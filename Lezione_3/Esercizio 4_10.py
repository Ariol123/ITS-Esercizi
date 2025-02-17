pizzas =["Margherita","Diavola","Capricosa","arrabiata","QuatroF","MiaPizza","AltraPizzzza"] 
print(f"The first three items in the list are {pizzas [0:3]}")

#Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.

media = len(pizzas)//2
print(media)
print(f"Three items from the middle of the list are {pizzas[media-1:media+2]}")