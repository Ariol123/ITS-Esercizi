'''name = input("nome")

if name == "Anna" or name == "Maria" or name == "Angela":
    print("ciao")
elif name == "Ric" or name == "Gg":
    print("ciao2")
else:
    print("ciao3")
    '''

PATH: str = "Lezione_1/lez111.py"
mode: str = "w"#w soprascrive il file
encoding: str = "utf-8"
message = "CiaoCiao"

file = open(PATH)
output: str = file.write(message)

print(output)
file.close()


with open("Lezione_1/lez111.py", "w") as file:
    print(file.read()) #context menager valido solo qui fuori non ha valore

#socket request

'''


'''