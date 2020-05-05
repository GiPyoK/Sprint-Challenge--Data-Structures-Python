import sys
import os
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        '../doubly_linked_list'
        )
    )
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        # First in, first out
        # Why is our DLL a good choice to store our elements?
        #   Queue inserts from the front and removes from the end,
        #   so DLL is an efficient data structure to acomplish this.

        self.storage = DoublyLinkedList()
        #self.size = 0

    def enqueue(self, value):
        self.storage.add_to_head(value)

    def dequeue(self):
        return self.storage.remove_from_tail()

    def len(self):
        return self.storage.length
