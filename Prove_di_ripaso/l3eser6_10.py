'''
6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

'''


favor_numb:dict[str:int] = {"Anna":[2,3,4], "Mario":[5,6], "gin":12,"Vera":23, "Maria":34}

for name, number in favor_numb.items():
    print(name,number)

# va bene cosi?
# o per il nome devo ciclare n volte le volte di quanto numeri ha---si puo fare?