import library
book = input("Enter Book Name: ")
print("1. Issue Book ")
print("2. Return Book ")
choice = int(input("Enter Your Choice "))
if choice == 1:
    library.issue_book(book)
elif choice ==2:
    library.return_book(book)
    days = int(input("Enter Number Of Days You Kept Book"))
    amount = library.fine(days)
    if amount == 0:
        print("No Fine")
    else:
        print("Fine Amount Rs",amount)
else:
    print("Invalid Choice")