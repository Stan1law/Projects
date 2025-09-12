from collections import deque
import heapq
from datetime import datetime, timedelta


class BorrowManager:
    """
    Manages borrowing and returning books.
    Uses a queue for borrow requests and a priority queue (heap) for overdue reminders.
    """

    def __init__(self, library):
        self.library = library
        self.borrow_queue = deque()  # Queue for borrow requests
        self.overdue_heap = []  # Priority queue for overdue books

        # Track borrowed books: {book_id: (user, due_date)}
        self.borrowed_books = {}

    def borrow_book(self, user, book_id):
        book = self.library.get_book(book_id)
        if book and book.available:
            book.available = False
            due_date = datetime.now() + timedelta(days=7)
            self.borrowed_books[book_id] = (user, due_date)
            user.borrow(book_id)
            # Add to overdue heap: (due_date, book_id)
            heapq.heappush(self.overdue_heap, (due_date, book_id))
            return True, due_date.strftime("%Y-%m-%d")
        return False, None

    def return_book(self, user, book_id):
        if book_id in self.borrowed_books and book_id in user.borrowed_books:
            book = self.library.get_book(book_id)
            book.available = True
            user.return_book(book_id)
            del self.borrowed_books[book_id]
            # Remove from overdue heap (rebuild heap)
            self.overdue_heap = [
                (due, bid) for due, bid in self.overdue_heap if bid != book_id
            ]
            heapq.heapify(self.overdue_heap)
            return True
        return False

    def get_overdue_books(self):
        now = datetime.now()
        overdue = []
        for due_date, book_id in self.overdue_heap:
            if due_date < now:
                user, _ = self.borrowed_books.get(book_id, (None, None))
                book = self.library.get_book(book_id)
                if user and book:
                    overdue.append((book, user, due_date.strftime("%Y-%m-%d")))
        # Sort by due date (priority queue property)
        overdue.sort(key=lambda x: x[2])
        return overdue
