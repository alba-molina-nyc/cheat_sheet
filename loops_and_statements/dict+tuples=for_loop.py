"""
"""



from venv import create


D = {'a': 1, 'b': 2, 'c': 3}

for key in D:
    print(key, '=>', D[key])             # use dict keys iterator and index



"""
using tuples in for loops to iterate through both keys and values in dictionaries 
using for loops, tuples, and .items() method
"""

create_tuple = list(D.items())
print(create_tuple, 'create tuple')


for (k, v) in create_tuple:
    print(k,v ,'kvkvkvkvcreatetuple')

    # OR 

for (key, value) in D.items():
    print(key, '---->', value)


N={'z': 9, 'y': 7, 'x': 5}

N.items()
print(N.items())

for k,v in N.items():
    print(k,v)




# TODO: figure what the .items() does
#TODO: p. 409 