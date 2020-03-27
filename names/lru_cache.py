from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.storage = DoublyLinkedList()
        self.limit = limit
        self.hashTable = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    # def get(self, key):
    #     node = self.storage.head
    #     while node != None:
    #         if list(node.value.keys())[0] == key:
    #             self.storage.move_to_front(node) # Most recently used, move to front
    #             return node.value[key]
    #         else:
    #             node = node.next
        
    #     # key does not exist
    #     return None

    def get(self, key):
        if key in self.hashTable:
            self.storage.move_to_front(self.hashTable[key]) # Most recently used, move to front
            return self.hashTable[key].value[1]
        
        # key does not exist
        return None


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):

        #  If the key-value is already in the storage, change the value
        if key in self.hashTable:
            self.hashTable[key].value = (key, value)
            self.storage.move_to_front(self.hashTable[key]) # Most recently used, move to front
            return

        # If the cache is already at the limit, delete the least recently used (tail)
        if self.storage.length >= self.limit:
            k = self.storage.tail.value[0]
            del self.hashTable[k]
            self.storage.remove_from_tail()
        
        # Add the key-value to the front of the storage
        self.storage.add_to_head((key, value))
        self.hashTable[key] = self.storage.head


    # def set(self, key, value):

    #     #  If the key-value is already in the storage, change the value
    #     node = self.storage.head
    #     while node != None:
    #         if list(node.value.keys())[0] == key:
    #             node.value[key] = value
    #             self.storage.move_to_front(node) # Most recently used, move to front
    #             return
    #         else:
    #             node = node.next

    #     # If the cache is already at the limit, delete the least recently used (tail)
    #     if self.storage.length >= self.limit:
    #         self.storage.remove_from_tail()
        
    #     # Add the key-value to the front of the storage
    #     self.storage.add_to_head({key : value})