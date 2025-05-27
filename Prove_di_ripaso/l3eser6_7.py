'''
6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.
'''


people:list[str:int] = [{"first_name":"Ari","last_name":"Spiro","age":42, "city":"Rome"},{"marco":23,"gim":54},{"jon":45,"hera":"amaizing"}]



for i in people:
    for key,value in i.items():
        print(key,value)