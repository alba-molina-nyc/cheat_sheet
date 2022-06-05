"""
tuples are immutable 
they are used to represent a fixed collection of items
i.e) - the components of a specific calendar date for instance 
tuples support mixed types and nesting just like lists and dictionaries 
"""

"""
🔆 for loops can be used in tuples
"""

T = (1, 2, 3, 4, 5)
print(len(T))

print(T[0], T[1], 'indexing') # indexing

print(T.count(3))


"""
since tuples are imutable, you cannot just add items into the tuple like you could mutable lists
so you need to create anew tuple for a new value 
"""

T = (2, 2) + T[1:]
print(T)