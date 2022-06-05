"""
closure AKA factory functions 

former describe a functional programming technique and latter a design pattern


"""

def maker(N):
    def action(X):                  # make and retain action
        return X ** N               # action retains N from enclosing scope
    return action

f = maker(2)                        # pass 2 to N argument
print(f)
print(f(3))                         # pass 3 to X
"""FACTORY FUNCTIONS are used by programs that need to generate event handlers on the fly in response to conditions at runtime """