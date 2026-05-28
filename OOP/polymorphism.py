# Polymorphism

class Bird:
    def sound(self):
        print("Bird sound")

class Crow(Bird):
    def sound(self):
        print("Caw Caw")

class Sparrow(Bird):
    def sound(self):
        print("Chirp Chirp")

birds = [Crow(), Sparrow(), Bird()]

for b in birds:
    b.sound()