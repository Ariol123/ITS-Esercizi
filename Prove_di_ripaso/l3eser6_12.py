'''
6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.
'''


favorite_places:dict[str,any] = {"anna":"Tirana","marco":"Roma","Jorgo":"Modena"}

favorite_places["mery"] = 23


favorite_places["jimmi"]= "Great"

print(favorite_places)



for name,place in favorite_places.items():
    print(f"My fiend {name} loves this citty: {place}!")

