import time
from lru_cache import LRUCache
from binary_search_tree import BinarySearchTree


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

start_time = time.time()

duplicates = []  # Return the list of duplicates in this data structure

bst = BinarySearchTree(names_1[0])
# Replace the nested for loops below with your improvements
for name_1 in names_1[1:]:  # O(n log n)
    bst.insert(name_1)
for name_2 in names_2:      # O(log n)
    if bst.contains(name_2):
        duplicates.append(name_2)

# nested for loop: O(n^2)
# since O(n log n) > O(log n), BST: O(n log n)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

start_time = time.time()

duplicates_1 = []
lruCache = LRUCache(10000)
for name_1 in names_1:      # O(n)
    lruCache.set(name_1, name_1)
for name_2 in names_2:      # O(n)
    if lruCache.get(name_2):
        duplicates_1.append(name_2)

end_time = time.time()
print (f"{len(duplicates_1)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# LRU Cache: O(2n) = O(n)