# Create a Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
print(f"Book created: {book.title} by {book.author} ({book.publication_year})")
print(f"Book ID: {book.id}")

#expected output: Book created: 1984 by George Orwell, 1949
