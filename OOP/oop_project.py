# Real Mini Example

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            print(self.name, "Passed")
        else:
            print(self.name, "Failed")

s1 = Student("Layana", 85)
s2 = Student("Ammu", 35)

s1.result()
s2.result()
