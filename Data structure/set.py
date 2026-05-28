# set
# A set is an unordered collection with no duplicates.

s = {1, 2, 3, 3}
print(s)


# Operations:
s = {1, 2, 3}

s.add(4)
s.remove(2)

print(s)


# Duplicate removal automatically
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)


# Empty Set
s = set()   # correct way
print(type(s))


# Adding Elements
s = {1, 2, 3}

s.add(4)
print(s)


# update() (add multiple values)
s = {1, 2, 3}

s.update([4, 5, 6])
print(s)


# Removing Elements
s = {1, 2, 3}

s.remove(2)
print(s)


# discard() (no error)
s = {1, 2, 3}

s.discard(10)  # safe
print(s)




# <<<----Set Operations---->>>

# Union (|)
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)


# Intersection (&)
a = {1, 2, 3}
b = {2, 3, 4}

print(a & b)


# <<< Set Methods >>>

# copy()
a = {1, 2, 3}
b = a.copy()

print(b)


# isdisjoint()
a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))


# issubset()
a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))


# issuperset()
a = {1, 2, 3}
b = {1, 2}

print(a.issuperset(b))



# Remove Duplicates
nums = [1, 1, 2, 3, 3, 4]

unique = list(set(nums))

print(unique)