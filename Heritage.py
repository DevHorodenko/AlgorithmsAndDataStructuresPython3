# Inheritance Example in Python
# This module demonstrates basic class inheritance, where the Car class inherits from the Transport class and adds its own attributes and methods.

class Transport():
    
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        pass

    def getName(self):
        return self.name
    
    def getWeight(self):
        return self.weight
    
    def getPrice(self):
        return self.price
    
class Car(Transport):

    def __init__(self, name, weight, price, brand):
        super().__init__(name, weight, price)
        self.brand = brand

    def getBrand(self):
        return self.brand


t = Car('Camaro', 500, 14999.99, "Chevrolet")

print(t.getName())
print(t.getWeight())
print(t.getPrice())
print(t.getBrand())