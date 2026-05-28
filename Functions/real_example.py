# Real Example Function

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

num = 10

if is_even(num):
    print("Even Number")
else:
    print("Odd Number")