# Project Example (Student Record System)

# Save student data into file

def add_student(name, marks):
    with open("students.txt", "a") as file:
        file.write(name + " - " + str(marks) + "\n")

add_student("Layana", 90)
add_student("Ammu", 80)