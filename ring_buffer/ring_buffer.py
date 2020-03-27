from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the DLL is empty, add to head and current becomes the head
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
            return
        
        # if the DLL is at the capacity, overide the oldest(current.next)
        if self.storage.length == self.capacity:
            # if the current is the tail, overwrite the head
            if self.current == self.storage.tail:
                self.storage.head.value = item
                self.current = self.storage.head
            # else if the current.next exists, overwrite current.next
            else:
                self.current.next.value = item
                self.current = self.current.next
        # else if the storage is not at the capacity, add value to tail
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        cursor = self.storage.head
        
        if cursor == None:
            return list_buffer_contents
        
        while cursor:
            list_buffer_contents.append(cursor.value)
            cursor = cursor.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------
# Another method of implementing a ring buffer uses an array (Python List) 
# instead of a linked list. 
# What are the advantages and disadvantages of using this method? 
#   - can use Python's built in array(list)
#   - get method is more efficient
# What disadvantage normally found in arrays is overcome with this arrangement?
#   - because current index being tracked, it required no iteration through the list

class ArrayRingBuffer:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.current = None
        self.stored = 0

    def append(self, item):
        # if empty array, append to first item
        if self.current == None:
            self.current = 0
            self.storage[0] = item
            self.stored += 1
        else:
            # if the current is at the end of the array, move the index to 0
            if self.current == len(self.storage) - 1:
                self.current = 0
            # if not, increament the current
            else:
                self.current += 1
                self.stored += 1
            # append item
            self.storage[self.current] = item

    def get(self):
        # if number of stored item equals the length of list, return storage
        if self.stored == len(self.storage):
            return self.storage
        # else, copy storage by value and remove any prepopulated 0's
        else:
            return self.storage[ : self.stored]
