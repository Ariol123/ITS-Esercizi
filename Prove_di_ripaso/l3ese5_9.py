'''
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.
'''


lista:list[str] = []
if  lista == []:
    print ("We need some name")

for name in lista:

    if name.lower() == "admin":
        
        print(f"Mitico {name}, would you like to see a status report?")
    else:
        print(f"Ciao {name} benvenuto!")


