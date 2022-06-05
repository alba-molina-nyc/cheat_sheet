"""

nested functions and scope

"""
x = 99                                                 # declare global x

def f1():                                              # define f1
    x = 88                                             # declare local x 
    def f2():                                          # define nested function f2
        print(x)                                       # print x 88 bc LEGB rule enclosing def local
    f2()                                               # call f2

f1()                                                   # call f1


