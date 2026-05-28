a = float(input("Enter A: "))
b = float(input("Enter B: "))

print("1.Add  2.Sub  3.Mul  4.Div")
choice = input("Choose operation: ")

if choice == "1":
    print(a + b)
elif choice == "2":
    print(a - b)
elif choice == "3":
    print(a * b)
elif choice == "4":
    print(a / b)
else:
    print("Invalid choice")