"""
return functions, in the ex 1 
the call to action is really running the function we named f2 when f1 ran
this works because functions are objects in python, and like everything else it can be passed as return values from other functions

Most importantly: f2 remembers the enclosing scope's X in f1 even though f1 is no longer active 

"""
# EX 1
x = 99                                          # global var
def f1():
    x = 88                                      # local var
    def f2():
        print(x)
    return f2                                   # return f2 but does not call it

action = f1()                                   # Make, return function 
action()                                        # call it, now prints 88 