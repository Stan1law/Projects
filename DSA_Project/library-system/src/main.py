from library import Library  # Uses hash table/trie for book search
from borrow_manager import (
    BorrowManager,
)  # Uses queue for borrow requests, priority queue for overdue
from user import User  # Represents a student/user


class LibrarySystem:
    def __init__(self):
        # Initialize the library and borrow manager
        self.library = Library()
        self.borrow_manager = BorrowManager(self.library)
        self.users = {}
        self.last_search_results = []

    def run(self):
        print("============================")
        print(" Library Management System")
        print("============================")
        print("Commands:")
        print("1. Search for books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Show overdue books")
        print("5. Exit")
        while True:
            command = input("\nEnter command number (1-5): ").strip()
            if command == "1":
                self.search_books()
            elif command == "2":
                self.borrow_book()
            elif command == "3":
                self.return_book()
            elif command == "4":
                self.show_overdue()
            elif command == "5":
                print("Exiting the library system.")
                break
            else:
                print("Invalid command. Please try again.")

    def search_books(self):
        search_term = input("Enter book title, author, or keyword: ")
        results = self.library.search_books(search_term)
        self.last_search_results = results
        if results:
            print("Results:")
            for idx, book in enumerate(results, 1):
                print(f"{idx}. {book}")
            print("To borrow, use command 2 and enter the number of the book.")
        else:
            print("No books found.")

    def borrow_book(self):
        if not self.last_search_results:
            print("Please search for books first (command 1).")
            return
        user_id = input("Enter your user ID: ")
        number = input("Enter the number of the book to borrow: ")
        try:
            idx = int(number) - 1
            if idx < 0 or idx >= len(self.last_search_results):
                print("Invalid number.")
                return
            book = self.last_search_results[idx]
            if user_id not in self.users:
                self.users[user_id] = User(user_id)
            success, due_date = self.borrow_manager.borrow_book(
                self.users[user_id], book.book_id
            )
            if success:
                print(f"Borrowed successfully. Due in 7 days (Due date: {due_date}).")
            else:
                print("Failed to borrow the book. It may be unavailable.")
        except ValueError:
            print("Please enter a valid number.")

    def return_book(self):
        user_id = input("Enter your user ID: ")
        book_id = input("Enter the book ID to return: ")
        if user_id in self.users:
            success = self.borrow_manager.return_book(self.users[user_id], book_id)
            if success:
                print("Book returned successfully.")
            else:
                print("Failed to return the book. It may not be borrowed by you.")
        else:
            print("User not found.")

    def show_overdue(self):
        overdue_list = self.borrow_manager.get_overdue_books()
        if overdue_list:
            print("Overdue Books (sorted by due date):")
            for book, user, due_date in overdue_list:
                print(f"{book} borrowed by {user.user_id}, due on {due_date}")
        else:
            print("No overdue books.")


if __name__ == "__main__":
    system = LibrarySystem()
    system.run()
