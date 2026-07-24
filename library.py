def issue_book(book_name):
    print(book_name,"has been issued Successfully")
def return_book(book_name):
    print(book_name,"has been return Successfully")
def fine(days):
    if days > 7:
        return(days - 7) * 10
    else:
        return 0