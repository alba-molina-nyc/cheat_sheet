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

