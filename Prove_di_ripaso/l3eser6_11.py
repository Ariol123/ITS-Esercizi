'''
6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.


'''

cities:dict[str,any] = {"tirana":""}
#cities = {"roma":""}
#cities = {"bari":""}



information:dict[str,any] = {"cauntry":"Albania","popolation":[3,"milion_people"],"fact":"beautiful"}                        
                        

for keyx in cities:
    for key,value in information.items():
        print(f"La citta {keyx} si trova in {key} e ha {value}")