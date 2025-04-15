from persona import Persona
from studente import Studente

#creo un oggetto p della classe persona
p: Persona = Persona("Arjol","Spirollari", 42)


#Visualizzo le inf dell' oggetto p
print(p)

#crea un oggetto studente1 della classe Studente
studente1: Studente = Studente("Mario", "Rossi", 20, "")

print(studente1)
print(studente1.getAge())


# controllo se studente1 e instanza della classe class
# isinstance(obj, class)--True else False

if isinstance(studente1, Studente):
    print("\nstudente e istanza della classe Student")

if isinstance(studente1, Persona):
    print(f" Studente1 e oggetto di tutte e due le classi")

if isinstance(p, Persona):
    print(" e un oggetto della classe Persona")

if isinstance(p, Studente):
    print (f" è un oggeto di due clasi Studente e Persona")
else:
    print(f" è un oggetto della classe Persona e non Studente")


'''
controllo che la classe studente e sottoclasse di persona
controla se class1 e sotto class di class2
True e False

'''
if issubclass(Studente, Persona):
    print(f"la class Studente e sottoclasse della class Persona")
