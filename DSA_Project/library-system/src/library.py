from book import Book


class Library:
    """
    Library class uses a hash table (dictionary) for book storage and search.
    """

    def __init__(self):
        # Example books
        self.books = {
            "B102": Book(
                "B102",
                "Intro to Data Structures",
                "Jane Smith",
                ["data structures", "intro"],
            ),
            "B210": Book(
                "B210",
                "Data Structures in Java",
                "John Doe",
                ["data structures", "java"],
            ),
            "B301": Book(
                "B301", "Python Algorithms", "Alice Lee", ["python", "algorithms"]
            ),
        }

    def search_books(self, term):
        """
        Search books by title, author, or keyword.
        """
        term = term.lower()
        results = []
        for book in self.books.values():
            if (
                term in book.title.lower()
                or term in book.author.lower()
                or any(term in kw.lower() for kw in book.keywords)
            ):
                results.append(book)
        return results

    def get_book(self, book_id):
        return self.books.get(book_id)
