import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# runtime: 29.82674503326416 seconds 
# O(n^2)

duplicates = []  # Return the list of duplicates in this data structure

bst = BinarySearchTree('names')
# loop throughu names_1 and add to tree
for names in names_1:
    bst.insert(names)
# if names in names_2 are duplicates add to duplicates list
for names in names_2:
    if bst.contains(names):
        duplicates.append(names)
# runtime: 0.43322157859802246 seconds 
# O(nlogn)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
