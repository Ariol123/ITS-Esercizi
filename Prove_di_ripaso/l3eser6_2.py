'''
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

'''

favor_numb:dict[str:int] = {"Anna":2, "Mario":5,"gin":12,"Vera":23, "Maria":34}

for name, number in favor_numb.items():
    print(name,number)