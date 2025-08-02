"""
Django Query Samples for relationship_app

This script demonstrates various Django ORM queries for the Author, Book, Library, and Librarian models.
Make sure to run this in a Django environment with the models properly set up.
"""

# Import Django setup (uncomment if running as standalone script)
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def query_all_books_by_author(author_name):
    """
    Query all books by a specific author.
    Uses ForeignKey relationship: Book -> Author
    """
    try:
        # Method 1: Get author first, then get books
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)

        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")

        # Method 2: Alternative using reverse relationship
        # books = author.book_set.all()

        return books

    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return None


def list_all_books_in_library(library_name):
    """
    List all books in a library.
    Uses ManyToManyField relationship: Library <-> Book
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()

        print(f"Books in {library_name}:")
        for book in books:
            print(f"- {book.title} by {book.author.name}")

        return books

    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None


def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    Uses OneToOneField relationship: Librarian -> Library
    """
    try:
        library = Library.objects.get(name=library_name)

        # Method 1: Get librarian using reverse relationship
        librarian = library.librarian

        print(f"Librarian for {library_name}: {librarian.name}")

        # Method 2: Alternative query
        # librarian = Librarian.objects.get(library=library)

        return librarian

    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'.")
        return None


def create_sample_data():
    """
    Create sample data for testing the queries.
    """
    # Create authors
    author1, created = Author.objects.get_or_create(name="J.K. Rowling")
    author2, created = Author.objects.get_or_create(name="George Orwell")
    author3, created = Author.objects.get_or_create(name="Jane Austen")

    # Create books
    book1, created = Book.objects.get_or_create(
        title="Harry Potter and the Philosopher's Stone",
        author=author1
    )
    book2, created = Book.objects.get_or_create(
        title="Harry Potter and the Chamber of Secrets",
        author=author1
    )
    book3, created = Book.objects.get_or_create(
        title="1984",
        author=author2
    )
    book4, created = Book.objects.get_or_create(
        title="Animal Farm",
        author=author2
    )
    book5, created = Book.objects.get_or_create(
        title="Pride and Prejudice",
        author=author3
    )

    # Create libraries
    library1, created = Library.objects.get_or_create(name="Central Library")
    library2, created = Library.objects.get_or_create(name="University Library")

    # Add books to libraries
    library1.books.add(book1, book2, book3)
    library2.books.add(book3, book4, book5)

    # Create librarians
    librarian1, created = Librarian.objects.get_or_create(
        name="Alice Johnson",
        library=library1
    )
    librarian2, created = Librarian.objects.get_or_create(
        name="Bob Smith",
        library=library2
    )

    print("Sample data created successfully!")


def main():
    """
    Main function to demonstrate all the queries.
    """
    print("=== Django Relationship Queries Demo ===\n")

    # Create sample data (uncomment to populate database)
    # create_sample_data()

    print("1. Query all books by a specific author:")
    query_all_books_by_author("J.K. Rowling")
    print()

    print("2. List all books in a library:")
    list_all_books_in_library("Central Library")
    print()

    print("3. Retrieve the librarian for a library:")
    retrieve_librarian_for_library("Central Library")
    print()

    # Additional query examples
    print("=== Additional Query Examples ===\n")

    # Query books with their authors (select_related for optimization)
    print("4. All books with authors (optimized query):")
    books_with_authors = Book.objects.select_related('author').all()
    for book in books_with_authors:
        print(f"- {book.title} by {book.author.name}")
    print()

    # Query libraries with their books count
    print("5. Libraries with book count:")
    libraries = Library.objects.prefetch_related('books').all()
    for library in libraries:
        print(f"- {library.name}: {library.books.count()} books")
    print()

    # Query authors with multiple books
    print("6. Authors with multiple books:")
    from django.db.models import Count
    authors_with_multiple_books = Author.objects.annotate(
        book_count=Count('book')
    ).filter(book_count__gt=1)
    for author in authors_with_multiple_books:
        print(f"- {author.name}: {author.book_count} books")


if __name__ == "__main__":
    main()