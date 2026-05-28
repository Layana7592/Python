# Function Scope

x = 10  # global variable

def test():
    x = 5  # local variable
    print("Inside function:", x)

test()
print("Outside function:", x)