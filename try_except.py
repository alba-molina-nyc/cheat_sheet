"""
handling errors w/ try and except
p.333

"""

# import if_statements


branch = {
    'spam': 1.25,
    'ham': 1.99,
    'eggs': 0.99
}


choice = 'bacon'
if choice in branch:
    print(branch[choice])
try: 
    print(branch[choice])
except KeyError:
    print('Bad')
else: 
    print('bad choice')


"""
TODO: learn the try and except 
Ch. 11 has more exceptions
"""