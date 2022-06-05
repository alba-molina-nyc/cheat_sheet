
"""
the x = x
means that the argument x will default to set the value of x in the enclosing scope- because the second x is evaluated before python steps into the nested def, it still refers to the x in f1

TODAY: Py automatically remembers any values required in the enclosing scope for use in nested def

"""
def f1():
    x = 88
    def f2(x=x):                # remembering enclosing scope with defaults
        print(x*x)
    f2()
f1()

"""
flat is better 
"""

def f1():
    x = 88                      # pass x along instead of nesting
    f2(x)                       # forward reference OK

def f2(x):
    print(x)                

f1()

def f3():
    x = 5
    f4(x-1)
    print(x, 'insidef3')

def f4(x):
    print(x, 'here')

f3()