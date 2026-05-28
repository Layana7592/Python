tasks = []

while True:
    print("\n1.Add 2.View 3.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        print("Tasks:", tasks)

    elif choice == "3":
        break