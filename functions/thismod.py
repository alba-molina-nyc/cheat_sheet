var = 99                                                        # global var

def local():
    var = 0                                                     # change local var

def glob1():
    global var                                                  # declare global
    var += 1                                                    # change global var

def glob2():
    var = 0
    import thismod    
    thismod.var += 1                                 
   

def glob3():
    var = 0                                                     # change local var
    import sys                                                  # import system table
    glob = sys.modules['thismod']                               # get module object
    glob.var += 1                                               # change global var


def test():
    print(var)
    local(); glob1(); glob2(); glob3();
    print(var)

import thismod                         
thismod.test()