class Animal:
    def __init__(self, name: str, legs: int):
        self.name= name
        self.legs = legs
    def setLegs(self, newlegs):
        self.legs = newlegs
    
    def  getLegs(self):
        return self.legs
    def  printInfo(self):
        print(self.name,self.legs)
    



        
    




animale1 = Animal("Tigre",4)
animale2 = Animal("Leone",4)


print(animale1.name)
print(animale2.name)




animale1.legs = 3

animale1.setLegs(6)

animale2.getLegs()

animale1.printInfo()