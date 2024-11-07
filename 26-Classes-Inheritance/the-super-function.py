class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        return f"{self.name} is enjoying the {food}"

class Dog(Animal):
    pass

#watson = Dog() 
watson = Dog("Watson")
print(watson.eat("bacon"))
print(watson.name)