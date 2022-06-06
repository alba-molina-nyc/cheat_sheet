"""
Python decorators
a decorator takes in a function, adds some functionality and returns it 
"""

def inc(x):
    return x + 1

def operate(func, x):                   # takes function above as an argument
    result = func(x)                # assign result which is what gets returned
    return result

print(operate(inc, 3)) # calls operate with the inc function as one and a three


"""
you can also define a function inside a function"""


def print_msg(message):
    greeting="Hi"

    def printer():
        print(greeting, message)

    printer()

print_msg("python is awesome")


"""functions can also return a function as a value

NOTICE: with this ex: inner function remembers values, variables in enclosing scope even if the outer function is done executing- such a function is called a CLOSURE"""

def print_msg(message):
    greeting="Hi"

    def printer():
        print(greeting, message)

    return printer

func = print_msg("python is da best")
func()

"""DECORATOR FUNCTIONS BELOW"""

def printer():                  # first function
    print("Hello world")

def display_info(func):         # decorator function that takes in a function, pass in func


    def inner():
        print("executing", func.__name__, "function") # func.__name__ is a dunder
        func()                  # calling functuon
        print("finished executing") # after function is executed 

    return inner            

printer()           # run printer function here
decorated_func = display_info(printer)          #use decorator function to run the same printer function this time
decorated_func()        # call the decorated_func


"""
code of above def printer(): code
when decorated_func = display_info(printer) gets called with the printer function which gets converted into the func argument
the inner function gets executed calls the func parameter and then gets executed 
as you can see the function was not changed there is a more elegant way of writing the above using decorators aka @
"""

