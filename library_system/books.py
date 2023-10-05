library_books = []
book = {}


def add_book(title, author):
    book = {"Title": str(title), "Author": str(author), "Availability": bool(True)}
    library_books.append(book)

def borrow_book(title):
    for book in library_books:
        if book['Title'] == title:
            if book['Availability'] == True:
                book['Availability'] = False
                return "You have borrowed the following book: " + title
            else:
                return "You can't borrow this book right now, as someone else has already borrowed it."
        else:
            return "Book not found in collection."
def return_book(title):
    for book in library_books:
        if book['Title'] == title:
            if book['Availability'] == False:
                book['Availability'] = True
                return "You have returned the following book: " + title
            else:
                return "This book is still in our collection and can't be returned."
        else:
            return "This book is not from our library."

def display_books():
    return library_books