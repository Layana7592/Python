# <<----For Loop---->>
for i in range(5):
    print(i)


# <<----For Loop with Start & End (range)---->>
for i in range(1, 11):
    print(i)


# <<----For Loop with Step Value (step loop)---->>
for i in range(0, 20, 2):
    print(i)


# <<----While Loop Basics (while loop)---->>
i = 0

while i < 5:
    print(i)
    i += 1


# <<----Break Statement (break)---->>
for i in range(10):
    if i == 5:
        break
    print(i)


# <<----Continue Statement (continue)---->>
for i in range(10):
    if i == 5:
        continue
    print(i)


# <<----Pass Statement (pass)---->>
for i in range(5):
    if i == 3:
        pass
    print(i)


# <<----Nested Loops (nested_loops)---->>
for i in range(3):
    for j in range(3):
        print(i, j)


# <<----Loop with List (list_loop)---->>
numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)


# <<----Loop with String (string_loop)---->>
text = "Python"

for char in text:
    print(char)


# <<----Loop with Index (enumerate)---->>
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


# <<----Reverse Loop (reverse_loop)---->>
for i in range(10, 0, -1):
    print(i)


# <<----Loop with Sum (sum_loop)---->>
numbers = [1, 2, 3, 4, 5]

total = 0

for num in numbers:
    total += num

print("Sum:", total)


# <<----Pattern Printing Example---->>
for i in range(1, 6):
    print("*" * i)


# <<----While Loop with Break Condition---->>
i = 1

while True:
    print(i)
    if i == 5:
        break
    i += 1


