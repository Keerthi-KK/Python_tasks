import math

class shape:
    def area(self):
        pass
    def perimeter(self):
        pass
    
class circle(shape):
    def __init__(self,r):
        self.radius=r
    def area(self):
        area1=math.pi* self.radius**2
        return area1
    def circumference(self):
        cir=2*math.pi*self.radius
        return cir
class triangle(shape):
    def __init__(self,a,b,c,h):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def area(self):
        return 0.5*self.b*self.h
    def perimeter(self):
        return self.a+self.b+self.c
class square(shape):
    def __init__(self,a):
        self.a=a
    def area(self):
        return a**2
    def perimeter(self):
        return 4*a
    
r=float(input("Enter radius:"))
c=circle(r).area()
p=circle(r).circumference()
print("Area of circle",c.area())
print("Circumference of circle ",c.circumference())

a1=triangle(7,8,9,10).area()
p1=triangle(7,8,9,10),perimeter()
print("Area of triangle",a1.area())
print("Perimeter of triangle",p1.perimeter())
