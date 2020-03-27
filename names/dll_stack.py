import sys
import os
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        '../doubly_linked_list'
        )
    )
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        # last in, first out
        # Why is our DLL a good choice to store our elements?
        #   Since DLL has tail pointer, it is easy to push and pop from the end(top).
        self.storage = DoublyLinkedList()
        # self.size = 0

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        return self.storage.remove_from_tail()

    def len(self):
        return self.storage.length
