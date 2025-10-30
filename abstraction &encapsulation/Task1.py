from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def  sound(self):
        pass
class  Lion(animal):
    def sound(self):
        print("Lion  roars")
class Tiger(animal):
    def sound(self):
        print("Tiger growls")
tiger=Tiger()
lion=Lion()
tiger.sound()
lion.sound()
