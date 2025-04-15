class libro:
    def __init__(self):
        self.titolo:str = ""
        self.autore:str = ""
        self.genere:list[str] = ""

    def set_titolo(self, titolo:str)->None:
        self.titolo = titolo
    
    def set_autore(self, nome:str)-> None:
        self.autore = nome

    def set_genere(self, tipo_genere:list[str])-> None:
        self.genere = tipo_genere

    def get_titolo(self)-> str:
        return self.titolo
    
    def get_autore(self) ->str:
        return self.autore
    
    def get_genere(self) -> list[str]:
        return self.genere
    
class Biblioteca:
    def __init__(self):
        self.libri:list[libro] = []

    def set_libro(self, libro:libro) -> None:
        self.libri.append(libro)

    def get_titoli(self) ->str:
        for item in self.libri:
            print(item.get_titolo())
    
    def get_info(self) -> None:
        for item in self.libri:
            print(item.get_titolo(), item.get_autore(), item.get_genere())


collezione:Biblioteca = Biblioteca()

libro1:libro = libro()
libro1.set_titolo("Il picolo principe")
libro1.set_autore("Sconosciuto")
libro1.set_genere("Narrativa")


collezione.set_libro(libro1)

libro2:libro = libro()
libro2.set_titolo("Harry Poter")
libro2.set_autore("JK Rowling")
libro2.set_gerere(["Narrativa"],["Fantasy"])

collezione.set_libro(libro2)

Biblioteca