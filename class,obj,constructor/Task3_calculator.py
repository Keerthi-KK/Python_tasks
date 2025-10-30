class Calculator:
    def __init__(self):
        pass
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            return "cannot divide by 0"
        return a/b
calc=Calculator()
print("Addition:",calc.add(10,5))
print("Subtraction:",calc.sub(20,7))
print("Multiplication:",calc.mul(5,10))
print("Division:",calc.div(6,3))
