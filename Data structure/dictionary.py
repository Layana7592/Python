# Dictionary
# A dictionary stores key-value pairs.

student = {
    "name": "Layana",
    "age": 22
}

print(student)


# Access values:
print(student["name"])


# Update values:
student["age"] = 23


# Add new key:
student["city"] = "Kannur"


# Loop dictionary:
for key, value in student.items():
    print(key, value)


# Accessing Values
student = {"name": "Layana", "age": 22}

print(student["name"])
print(student["age"])


# Adding Items
student = {"name": "Layana"}

student["age"] = 22
student["city"] = "Kannur"

print(student)


# Updating Values
student = {"name": "Layana", "age": 22}

student["age"] = 23

print(student)



# Removing Items
student = {"name": "Layana", "age": 22}

student.pop("age")
print(student)


# <<<<< Nested Dictionary >>>>>
students = {
    "student1": {"name": "A", "age": 20},
    "student2": {"name": "B", "age": 21}
}

print(students["student1"]["name"])

