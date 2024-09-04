# Initialize an empty list to store book information
library = []


# Function to add a new book
def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    book_author = input("Enter Book Author: ")
    book_price = float(input("Enter Book Price: "))
    book_publisher = input("Enter Book Publisher: ")

    # Create a dictionary for the new book
    book = {
        "id": book_id,
        "name": book_name,
        "author": book_author,
        "price": book_price,
        "publisher": book_publisher
    }

    # Add the book to the library list
    library.append(book)
    print("Book added successfully!\n")


# Function to display all books
def display_books():
    if not library:
        print("No books in the library.")
        return

    print("\nBooks in Library:")
    for book in library:
        print(
            f"ID: {book['id']}, Name: {book['name']}, Author: {book['author']}, Price: {book['price']}, Publisher: {book['publisher']}")
    print()


# Function to update the price of a book
def update_price():
    book_id = input("Enter Book ID to update price: ")
    found = False

    for book in library:
        if book['id'] == book_id:
            new_price = float(input(f"Enter new price for '{book['name']}': "))
            book['price'] = new_price
            found = True
            print("Book price updated successfully!\n")
            break

    if not found:
        print("Book not found.\n")


# Function to delete a book
def delete_book():
    book_id = input("Enter Book ID to delete: ")
    found = False

    for book in library:
        if book['id'] == book_id:
            library.remove(book)
            found = True
            print("Book deleted successfully!\n")
            break

    if not found:
        print("Book not found.\n")


# Main menu-driven loop
while True:
    print("Library Menu:")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Update Book Price")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        update_price()
    elif choice == '4':
        delete_book()
    elif choice == '5':
        print("Exiting the library system.")
        break
    else:
        print("Invalid choice. Please try again.\n")
