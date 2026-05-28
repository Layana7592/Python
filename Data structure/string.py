# String
# A string is a sequence of characters.

text = "Python"
print(text)


# Operations:
text = "Python"

print(text.upper())
print(text.lower())
print(len(text))


# String Indexing
text = "Python"

print(text[0])  # P
print(text[1])  # y
print(text[-1]) # n


# String Slicing
text = "Python"

print(text[0:4])   # Pyth
print(text[:3])    # Pyt
print(text[2:])    # thon


# String Length
text = "Python"

print(len(text))



# <<<----String Methods---->>>

# upper()
text = "python"
print(text.upper())


# lower()
text = "PYTHON"
print(text.lower())


# strip() (remove spaces)
text = "  Python  "
print(text.strip())


# replace()
text = "I like Java"
print(text.replace("Java", "Python"))


# split()
text = "I love Python"
print(text.split())


# join()
words = ["I", "love", "Python"]
print(" ".join(words))


# <<<<< String Concatenation >>>>>
a = "Hello"
b = "World"

print(a + " " + b)


# String Repetition
print("Hi " * 3)



# <<<<<< String Formatting >>>>>>>

# f-string (BEST METHOD)
name = "Layana"
age = 22

print(f"My name is {name} and age is {age}")


# Count Characters
text = "python"

print(text.count("p"))


