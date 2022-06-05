"""
py's most general iteration construct
it repeatedly 

when the test becomes false, control passes to the statement that follows the while block

the loop's body is executed repeatedly while the test at the top is true 
if the test is false to begin with, the body never runs and the while statement is skipped 

format


while test:       # loop test
    statements    # loop body
else:             # optional else
    statements    # run if did not exit the loop with break
"""


"""
BREAK 
jumps out of the closest enclosing loop(past the entire loop statement)

CONTINUE
jumps to the top of the closest enclosing loop(to the loop's header)

PASS
does nothing at all: it is an empty statement placeholder, used when the syntax requires a statement but you have nothing useful to say 

LOOP ELSE BLOCK 
runs if and only if the loop is exited normally, without hitting a break


while test:
    statements
    if test: break                    # exit loop now, skip else if present
    if test: continue                 # go to top of loop now, to test1
else: 
    statements                        # run if did not hit a break

"""

# CONTINUE 

x = 10
while x: 
    x = x -1 
    if x % 2 != 0:
        continue    # uses continue to skip off odd nums
    print(x, 'evens')

x = 10
while x: 
    x = x -1 
    if x % 2 == 0:
        continue    # uses continue to skip off even nums
    print(x, 'odds')

# BREAK 

while True: 
    name = input('Enter your name: ')
    if name == 'stop':
        break
    age = input('Enter your age')
    print('Hello', name, '=>', int(age) ** 2)


# LOOP ELSE 



