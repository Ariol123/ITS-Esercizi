from abc import ABC, update_abstractmethods




class Shape(ABC):
    @update_abstractmethods
    def __init__(self):
        pass

    @update_abstractmethods
    def area(self)-> float:
        pass


    @update_abstractmethods
    def shape(self) :
        pass