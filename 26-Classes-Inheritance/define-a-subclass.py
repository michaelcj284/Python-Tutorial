class Store():
    def __init__(self):
        self.owner = "Boris"

    def excliam(self):
        return "Lots of stuff to buy, come inside!"

class CoffeShop(Store):
    pass

startbucks = CoffeShop()

print(startbucks.owner)
print(startbucks.excliam())