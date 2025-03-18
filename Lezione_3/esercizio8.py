class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)
riccardo = Person("Riccardo.L", 20)
federico = Person("Federico",29)
rebecca = Person("Rebecca",19)

people = [alice,bob,riccardo,federico,rebecca]
print(bob.age)

if bob.age > alice.age:
    print(bob.age)
else:
    print(alice.age)
min=99
min_name = ""
for i in people:
    if i.age < min:
        min = i.age
        min_name=i.name
    
print(min_name)