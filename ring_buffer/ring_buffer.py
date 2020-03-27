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


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
