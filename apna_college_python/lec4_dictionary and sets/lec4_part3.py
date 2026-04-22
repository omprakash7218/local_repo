#     SET IN PYTHON
#     set is the collection of unordered items and each item 
#     is unique and immutable(elements){set itself is mutable but its elements are not}


nums = {2,4,6,7,2345}
set2 = {1,32,2,3,23,32,23,32,3,23,1,1,1,1,1,1}
print(type(set2))
print(set2)


collection = {2,3,45,"hello world", 7.34, True, 3}
print(collection)
print(len(collection))

raju = {}
print(type(raju))
raju2 = set()
print(type(raju2))


# methods in set

col1 = set()
col1.add(1)
col1.add(32)
col1.add(32)
col1.add("om")
col1.add(2)
# col1.add({1,2,2,"omprkaash"})  # since set , dict , list is mutable it cannot go into the set
col1.add(("asldfjl", 234,234,53,253))
print(col1) 

col1.remove("om")   # removes a specific value that you give 
print(col1)
# col1.clear()   # clear all the values len(col1) will give you 0
print(col1)
col1.pop()  # removes a random value
print(col1.pop())
print(col1)
col1.add(423)
col2 = {"om" , 2,23,423,4,23423,432,4234,1343,53,253}
# print(col1.union(col2))
print(col1.intersection(col2))
print(col1)

print(col1.clear())
print(len(col1))