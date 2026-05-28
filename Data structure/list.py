# List
# A list is an ordered, changeable collection.

numbers = [10, 20, 30, 40]
print(numbers)


# Common Operations:
nums = [1, 2, 3]

nums.append(4)
nums.insert(1, 100)
nums.remove(2)

print(nums)


# Loop in list:
for i in [1, 2, 3]:
    print(i)


# Creating  lists
numbers = [1, 2, 3, 4, 5]
names = ["Layana", "Ammu", "Riya"]
mixed = [1, "Hello", 3.5, True]

print(numbers)
print(names)
print(mixed)


# Indexing (Accessing Elements)
numbers = [10, 20, 30, 40]

print(numbers[0])   # first element
print(numbers[-1])  # last element


# Slicing
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])


# Updating List Elements
numbers = [1, 2, 3]

numbers[1] = 100

print(numbers)


# Adding Elements - append()
nums = [1, 2, 3]

nums.append(4)
print(nums)


# insert()
nums = [1, 2, 3]

nums.insert(1, 99)
print(nums)


# extend()
a = [1, 2]
b = [3, 4]

a.extend(b)
print(a)


# Removing Elements - remove()
nums = [1, 2, 3]

nums.remove(2)
print(nums)


# pop()
nums = [1, 2, 3]

nums.pop()
print(nums)


# pop(index)
nums = [1, 2, 3]

nums.pop(1)
print(nums)


# clear()
nums = [1, 2, 3]

nums.clear()
print(nums)


# Loop in List
nums = [1, 2, 3, 4]

for n in nums:
    print(n)


# List Length
nums = [1, 2, 3]

print(len(nums))


# Sorting
nums = [5, 2, 9, 1]

nums.sort()
print(nums)


# Reverse sort
nums = [5, 2, 9, 1]

nums.sort(reverse=True)
print(nums)


# Reverse List
nums = [1, 2, 3]

nums.reverse()
print(nums)


# Copy List
a = [1, 2, 3]

b = a.copy()

print(b)


# Count Elements
nums = [1, 2, 2, 3, 2]

print(nums.count(2))


# Find Index
nums = [10, 20, 30]

print(nums.index(20))



# <<------List Comprehension------>>
nums = [i for i in range(5)]
print(nums)


# Squares
squares = [i*i for i in range(6)]
print(squares)



# Even numbers
even = [x for x in range(10) if x % 2 == 0]
print(even)


# Nested List
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print(matrix[0])
print(matrix[1][1])


# Sum of List
nums = [1, 2, 3, 4]

total = sum(nums)
print(total)


# Max & Min
nums = [10, 20, 5, 30]

print(max(nums))
print(min(nums))
