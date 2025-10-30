from abc import ABC,abstractmethod
import math

class shape(ABC):
    @abstractmethod
    def  calcArea(self):
        pass
    @abstractmethod
    def  calcPerimeter(self):
        pass
    
class  Circle(shape):
    def __init__(self,r):
        self.radius=r
    def calcArea(self):
        return math.pi *self.radius**2
    def calcPerimeter(self):
        return 2*math.pi*self.radius
    
class Triangle(shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def calcArea(self):
        s=(self.a+self.b+self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    def calcPerimeter(self):
        return self.a+self.b+self.c
    
circle=Circle(5)
triangle=Triangle(3,4,5)
print("Area of a circle is :",circle.calcArea(),"perimeter of a circle",circle.calcPerimeter())
print("Area of a triangle is :",triangle.calcArea(),"perimeter of a triangle",triangle.calcPerimeter())

