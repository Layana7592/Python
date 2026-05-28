# Variable Length Arguments (*args)

def total(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    print("Total:", sum)

total(1, 2, 3, 4, 5)