
"""BELOW USES @ SYMBOL to do the exact same thing that the above code did
the decorator below only works with funcitons that have no parameters"""

def printer():               
    print("Hello world")

def display_info(func):        


    def inner():
        print("executing", func.__name__, "function") 
        func()                
        print("finished executing") 

    return inner     

@display_info
def printer():
    print("Hello world!")       

printer()


"""example with parameters"""




def smart_divide(func):
    def inner(a,b):
        print("dividing", a, "by", b)
        if b == 0:
            print("cannot divide by 0")
            return
        else:
            func(a,b)
    return inner


@smart_divide
def divide(a, b):
    return a/b

value1=divide(15, 3)
print(value1)

value2=divide(5, 0)
print(value2)


"""chaining decorators, 
in python a function can be decorated multiple times with different or same decorators"""


def star(func):
    def inner(arg):
        print("*" * 30)
        func(arg)
        print("*" * 30)
    return inner

def percent(func):
    def inner(arg):
        print("/" * 30)
        func(arg)
        print("/" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

printer("decoators are amazing")



"""below is the example with out using the decorator "a" symbol: 


def printer(msg):
    print(msg)

printer = star(percent(printer))


"""