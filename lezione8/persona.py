class Persona:

    def __init__(self, name: str, lastname: str, age: int) -> None:

        self.name: str = name
        self.lastname: str = lastname
        self.age: int = age

    def displayData(self) -> None:
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}")


class Persona:
    def __init__(self) -> None:
        self.name:str = ""
        self.lastname: str = ""
        self.age: int = 0

    def setName(self, name) ->None:
        self.name: str = name

    def setLastname(self, lastname) -> None:
        self.lastname: str =lastname

    def setAge(self, age) -> None:
        if age < 0 or age >130:
            self.age = 0
        else:
            self.age :int = age
    
    def getName(self) -> str:
        return self.name
    
    def getLastneme(self) ->str:
        return self.lastname
    
    def getAge(self) -> int:
        return self.age
    def displayData(self) -> None:
        print(f"Nome{self.name}\nConiome: {self.lastname}\nEtà: {self.age}")
