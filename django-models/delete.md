# Retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")
print(f"Book to delete: {book.title} by {book.author}")

# Delete the book
book.delete()
print("Book deleted successfully")

# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
print(f"Total books after deletion: {len(all_books)}")

# Try to retrieve the deleted book (this should raise an exception)
try:
    deleted_book = Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("Confirmed: Book no longer exists in database")

#expected output: Confirmed: Book no longer exists in database
