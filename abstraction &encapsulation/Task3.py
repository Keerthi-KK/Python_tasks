from abc import ABC,abstractmethod
import math

class shape(ABC):
    @abstractmethod
    def  calcVolume(self):
        pass
 
    
class  Cylinder(shape):
    def __init__(self,r,h):
        self.radius=r
        self.height=h
    def calcVolume(self):
        return math.pi *self.radius**2*self.height

    
class  Cone(shape):
    def __init__(self,r,h):
        self.radius=r
        self.height=h
    def calcVolume(self):
        return (1/3)*math.pi *self.radius**2*self.height

class  Sphere(shape):
    def __init__(self,r):
        self.radius=r
    def calcVolume(self):
        return (4/3)*math.pi *self.radius**3
    
cylinder=Cylinder(5,6)
cone=Cone(3,4)
sphere=Sphere(5)
print("Volume  of a cylinder is :",cylinder.calcVolume())
print("Volume  of a cone is :",cone.calcVolume())
print("Volume  of a sphere is :",sphere.calcVolume())


