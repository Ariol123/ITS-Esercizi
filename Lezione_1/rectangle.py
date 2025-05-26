from esercizio_20_05 import Shape
import math

class Rectangle(Shape):
    def __init__(self, b: float, h: float):
        self.__b= b
        self.__h = h

    def area(self)-> float:
        return self.__b * self.__h
    
    def perimeter(self):
        return (self.__b + self.__h ) * 2
    
    def base(self):
        return self.__b
    
    def height(self):
        return self.__h
    