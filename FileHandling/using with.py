#----------------------------
# File Handling using with
#----------------------------


with open("data.txt", "w") as file:
    file.write("Using with statement in Python")


#----------------------------
# Read using with
#----------------------------


with open("data.txt", "r") as file:
    content = file.read()
    print(content)


#----------------------------
# Check if File Exists (os module)
#----------------------------


import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File not found")