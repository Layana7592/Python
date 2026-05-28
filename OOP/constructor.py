# Constructor

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(self.brand, self.model)

c1 = Car("Toyota", "Innova")
c1.display()