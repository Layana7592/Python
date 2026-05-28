print("Hello, Python!")

# =========================
# VARIABLES SECTION
# =========================

name = "Layana"
age = 22
height = 5.5

print(name)
print(age)
print(height)

# =========================
# Input & Output
# =========================

name = input("Enter your name: ")
print("Hello", name)

# =========================
# Data Types
# =========================

a = 10
b = 3.5
c = "Python"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# =========================
# Conditional Statements
# =========================

age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")

# =========================
# Loops
# =========================

for i in range(5):
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1

# =========================
# Functions
# =========================

def greet(name):
    print("Hello", name)

greet("Layana")

# =========================
# Strings
# =========================

text = "Python Basics"

print(text.upper())
print(text.lower())
print(len(text))

# =========================
# Lists
# =========================

numbers = [1, 2, 3, 4]

numbers.append(5)

print(numbers)


# =========================
# Basic Operators
# =========================

a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)


