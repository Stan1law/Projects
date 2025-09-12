class Book:
    """
    Book class represents a book in the library.
    """

    def __init__(self, book_id, title, author, keywords):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.keywords = keywords
        self.available = True  # Default to available

    def __str__(self):
        return f"{self.title} by {self.author} (ID: {self.book_id}){' [Available]' if self.available else ' [Borrowed]'}"
