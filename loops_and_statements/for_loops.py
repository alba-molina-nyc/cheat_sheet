"""
generic iterator in python, it can step through the items in any ordered sequence or other iterable objects

it works on strings, lists, tuples, and other built in iterables and the classes you make too 

for target in object:           # assign the object items to target
    statements                  # repeated loop body: use target
else:                           # optional else part
    statements                  # if we do ot hit a 'break'


for target in object: 
    statements
    if test:
        break                   # exit loop now, skip else
    if test: continue           # go to top of loop now
else: 
    statements                  # if we did not hit a 'break'

            x1,     x2,     x3
for x in ["spam", "eggs", "ham"]:
    print(x) 

"""

for x in ["spam", "eggs", "ham"]:
    print(x)        

sum = 0
for x in [1,2,3,4]:
    sum = sum + x 
    print(sum, 'sum')


"""
sum = 0

for x in [1,2,3,4]:
    sum = sum + x 
    print(sum, 'sum')

# iteration 1 for x(0) in [1,2,3,4]:
    sum = 0 + 1
    sum = 1

# iteration 2 for x(1) in [1,2,3,4]:
    sum = sum(1) + 2
    sum = 3

# iteration 3 for x(2) in [1,2,3,4]:
    sum = sum(3) + 3
    sum = 6



"""








"""
list comprehensions: will run faster && this could matter for larger data sets
"""

squares = [ x ** 2 for x in [1,2,3,4,5]] # the part following the '=' is a list comprehension
print(squares)

"""
or you can use a for loop: 
"""

squares = []

for x in [1,2,3,4,5]:
    squares.append(x ** 2)

    print(squares)


"""
Nested for loops

the outer loop scans the keys list and in the inner loop scans the items list for each 

the nesting of the loop else in the below example is critical because it is indented to the same level as the header line of inner for loop so it is associate with the inner loop, not the if or the outer loop
"""

items = ["aaa", 1111, (4,5), 2.01, 'yxxx']            # a set of objects
tests = [(4,5), 3.14, 1111, 902, 'yxxx']              # keys to search for

for key in tests:                           # for all keys
    for item in items:                      # for all items
        if item == key:                     # check for match
            print(key, 'we found a key')
            break
    else: 
        print(key, 'not found')


seq1 = "spam"
seq2 = "scam"

res = []

for x in seq1:
    if x in seq2:
        res.append(x)
        print(res, '3insideif')
    print(res, '2if')
print(res, '1for')


# TODO: range vs slicing and 