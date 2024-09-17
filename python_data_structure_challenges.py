# Task 1: Library System Enhancement

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book():
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    book = (title, author)
    if book not in library:
        library.append(book)
    else:
        print("Book already exists in the library.")
add_book()
print(library)