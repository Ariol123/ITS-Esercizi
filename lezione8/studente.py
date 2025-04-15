from persona import Persona

#classe Studente eredita dalla classe Persona
class Studente(Persona):


    '''
    Attributi della classe persona
    self.name: str
    self.lastname: str
    salf.age: int

    Attributi dello Studente
    self.matricola: str

    
    '''

# inizializzare un oggetto della classe Studente
    def __init__(self, name: str, lastname: str, age: str, matricola: str):
       #inizializzo la classe persona richiamando il metodo __init__
        super().__init__(name, lastname, age)

        self.setMatricola(matricola)
#metodo che imposta il valore del attributo
    def setMatricola(self, matricola: str)-> None:
        if matricola:
            self.matricola = matricola
        else:
            print("\nErrore! non si puo iniziare una stringa vuota")
    
    def getMatricola(self)->SyntaxWarning:
        return self.matricola
    
#ridefinire il metodo __str__ 
    def __str__(self) -> str:
        return (f"\nNome: {self.name}\nCognome: {self.getLastname()}\nMatricola: {self.getMatricola()}")
   
