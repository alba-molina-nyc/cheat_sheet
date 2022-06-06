
"""BELOW USES @ SYMBOL to do the exact same thing that the above code did"""

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
