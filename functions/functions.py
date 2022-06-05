"""

def = function definition 

def function_name(x,y):                                     # def defines the function followed by function name inside (params)
    return x * y                                            # function body and return statement 


function_name(3,2)                                          # function call

"""

# EX 1
def first_func(x,y):
    return x * y

print(first_func(2,3))


# EX 2

"""
finds dupes in the result
"""

def intersect(seq1, seq2):
    res = []                                                # initialize empty list
    for x in seq1:                                          # scan seq1
        if x in seq2:                                       # search common items
            res.append(x)                                   # add to the end
    return res 

s1 = "SCAMMER"
s2 = "SPAMMER"
intersect(s1, s2)                                           # calling function && passing on two strings we defined above
print(intersect(s1, s2))

"""
list comprehension expression 
that does the same thing done above
"""
no_dupes=[x for x in s1 if x in s2]
print(no_dupes)

"""
Function Scope 
"""

x = 99                                                  # global scope

def func(y):                                            # y and z assigned in function: locals
    z = x + y                                           # x is a global 
    return z

func(1)                                                 # calling the function
print(func(1), 'sdfsdf') 


"""
global variables inside functions
"""

xx = 77

def func():
    global xx
    xx = 99 

func()
print(x)                                                # changing x inside function also changes x outside of function


"""
p.495
"""

y = 1
z = 2
def all_global():
    global xx
    x = y + z

all_global()
print(all_global())


"""
look into non locals too

"""

def tester(start):
    state = start
    def nested(label):
        nonlocal state              # remembers state from enclosing scope
        print(label, state)
        state += 1
    return nested

f = tester(555)
f('spammy')




