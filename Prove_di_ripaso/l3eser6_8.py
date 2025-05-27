'''
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet. 

'''
lista:list[any] = [{"dog":"Luigi"},{"Cat":"John"},{"Rat":"Micky"}]

for dict in lista:
    for animal in dict:
        print(f"THe best friend of man is {animal}")
