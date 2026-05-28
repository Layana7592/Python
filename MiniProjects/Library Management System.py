books = []

while True:
    print("\n1.Add Book 2.View Books 3.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)

    elif choice == "2":
        print("Books:", books)

    elif choice == "3":
        break