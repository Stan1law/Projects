class Node:
    def __init__(self, book, priority):
        self.book = book
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, book, priority):
        new_node = Node(book, priority)
        if self.head is None or self.head.priority > priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        removed_node = self.head
        self.head = self.head.next
        return removed_node.book

    def peek(self):
        if self.is_empty():
            return None
        return self.head.book

    def display(self):
        current = self.head
        while current is not None:
            print(f'Book: {current.book.title}, Due Date: {current.book.due_date}')
            current = current.next