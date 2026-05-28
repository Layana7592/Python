balance = 1000

print("1.Deposit 2.Withdraw 3.Balance")
choice = input("Enter choice: ")

if choice == "1":
    amt = int(input("Enter amount: "))
    balance += amt
    print("New Balance:", balance)

elif choice == "2":
    amt = int(input("Enter amount: "))
    if amt <= balance:
        balance -= amt
        print("New Balance:", balance)
    else:
        print("Insufficient balance")

elif choice == "3":
    print("Balance:", balance)

else:
    print("Invalid option")