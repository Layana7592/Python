# Instance vs Class Variables

class Student:
    school = "ABC School"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

s1 = Student("Ammu")
s2 = Student("Riya")

print(s1.name, s1.school)
print(s2.name, s2.school)