# Retrieve the book we just created
all_books = Book.objects.all()
print(f"Total books: {len(all_books)}")
for book in all_books:
    print(f"- {book.title} by {book.author} ({book.publication_year})")

#expected output:  1984 by George Orwell (1949)
