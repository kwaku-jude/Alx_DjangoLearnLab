# Django Bookshelf App - CRUD Operations

This document contains all CRUD (Create, Read, Update, Delete) operations performed on the Book model in the Django shell.

## Setup Commands
```python
# Import the Book model
from bookshelf.models import Book
```

## 1. CREATE Operation

### Command:
```python
# Create a Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
print(f"Book created: {book.title} by {book.author} ({book.publication_year})")
print(f"Book ID: {book.id}")
```

### Output:
```
Book created: 1984 by George Orwell (1949)
Book ID: 1
```

---

## 2. RETRIEVE Operation

### Command:
```python
# Retrieve the book we just created
book = Book.objects.get(title="1984")

# Display all attributes
print(f"ID: {book.id}")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")

# Show all books
all_books = Book.objects.all()
print(f"Total books: {len(all_books)}")
```

### Output:
```
ID: 1
Title: 1984
Author: George Orwell
Publication Year: 1949
Total books: 1
```

---

## 3. UPDATE Operation

### Command:
```python
# Retrieve and update the book
book = Book.objects.get(title="1984")
print(f"Original title: {book.title}")

book.title = "Nineteen Eighty-Four"
book.save()

print(f"Updated title: {book.title}")
```

### Output:
```
Original title: 1984
Updated title: Nineteen Eighty-Four
```

---

## 4. DELETE Operation

### Command:
```python
# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
print(f"Book to delete: {book.title} by {book.author}")

book.delete()
print("Book deleted successfully")

# Confirm deletion
all_books = Book.objects.all()
print(f"Total books after deletion: {len(all_books)}")

try:
    deleted_book = Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("Confirmed: Book no longer exists in database")
```

### Output:
```
Book to delete: Nineteen Eighty-Four by George Orwell
Book deleted successfully
Total books after deletion: 0
Confirmed: Book no longer exists in database
```

---

## Summary

All CRUD operations were successfully performed:
- ✅ **CREATE**: Book instance created and saved to database
- ✅ **READ**: Book retrieved and all attributes displayed
- ✅ **UPDATE**: Book title updated from "1984" to "Nineteen Eighty-Four"
- ✅ **DELETE**: Book successfully deleted and deletion confirmed

The Book model is working correctly with all database operations.