expenses = []

while True:
    print("\n1.Add Expense 2.View Total 3.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        amt = float(input("Enter expense: "))
        expenses.append(amt)

    elif choice == "2":
        print("Total Expense:", sum(expenses))

    elif choice == "3":
        break