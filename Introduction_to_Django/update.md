# Retrieve the book to update
book = Book.objects.get(title="1984")
print(f"Original title: {book.title}")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

print(f"Updated title: {book.title}")

# Verify the update by retrieving again
updated_book = Book.objects.get(id=book.id)
print(f"Verified title from database: {updated_book.title}")

#expected output : Verified title from database: Nineteen Eighty-Four
