"""
Ch. 12 

if test1:
    statements1
elif test2:
    statements2
else:
    statements3

all parts of an if statement are optional, except if test and its associated statements

when it is run python executes the statements nested under the first test that is true, or the else part if all the tests are false

"""

x = 'killer rabbit'

if x == 'roger':
    print('shave and a haircut')
elif x == 'bugs':
    print('what is up doc?')
else:
    print('run away')

branch = {
    'spam': 1.25,
    'ham': 1.99,
    'eggs': 0.99
}

print(branch.get('spam', 'Bad Choice'))

print(branch.get('bacon', 'Bad Choice'))

choice = 'bacon'
if choice in branch:
    print(branch[choice])
else: 
    print('bad choice')

x = 1
if x:
    print(x)
    y = 2
    print(y)
    if y:
        print('block2')
    print('block1')
print('block0')


"""
TERNARY
a fancy way to write if else statements
"""



if X: 
    A = Y
else:
    A = Z 

# AKA

A = Y if X else Z