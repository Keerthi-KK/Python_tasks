import math

class circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        area1=math.pi* self.radius**2
        return area1
    def circumference(self):
        cir=2*math.pi*self.radius
        return cir
r=float(input("Enter radius:"))
c=circle(r)
print("Area of circle",c.area())
print("Circumference of circle ",c.circumference())
