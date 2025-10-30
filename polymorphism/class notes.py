class Cat:
    def __init__(self,name):
        print(f"I am {name}")
    def info(self,name,age):
        print(f"Cat name is {name} and its age is {age}")
    def make_sound(self):
        print("Meow")
class Dog(Cat):
    def __init__(self,name):
        super().__init__("Kitty")
        print(f"I am {name}")
    def info(self,name,age):
        super().info("Kitty","7")
        print(f"Dog name is {name} and its age is {age}")
    def make_sound(self):
        super().make_sound()
        print("Bark")


obj2 = Dog("Tommy")
obj2.info("Fluffy", "25")
obj2.make_sound()
