"""

Dicts consists of key:value pairs
you can index a dict by key to fetch and change the key's associated values

"""

D = {
    'food': 'pizza',
    'quantity': 4,
    'color': 'red'
}  # creates dict
print(D)

fetch_food = D['food'] # fetch value 
print(fetch_food) 

D['quantity'] += 1  # add 1 to quantity value
print(D)

DD = {} # creates empty dictionary 

DD['name'] = 'Victor'
DD['job'] = 'lawyer'
DD['age'] = 26



print(DD)

# double nesting 

rec = {'name': {'first': 'Bob', 'last': 'Smith'},
'jobs': ['dev', 'mgr'],
'age': 40}

print(rec)

print(rec['name']['last']) # access

rec['jobs'].append('janitor') # add jobs
print(rec)


DDD = {
    'a': 1,
    'b': 2,
    'c': 3
}

DDD['e'] = 99 # add e

print(DDD)


"""
KeyError: 'f'
Accessing a key that does not exist in the dict 
DDD['f'] 
print(DDD)

"""

if not 'f' in DDD:
    print('missing') # this is a sole selection statement 


"""
Sorting Keys && For Loops

"""

D_01 = {'h': 4, 'a': 1, 'b': 2, 'c': 3}

KS = list(D_01.keys()) # access keys method
print(KS)

VS = list(D_01.values()) # access values method
print(VS)

KS.sort() # sort method
print(KS)


for key in KS: 
    print(key, '->', D_01[key])


for c in 'spam-python':
    print(c.upper()) # for every single letter in this iteration capitalize it 

x = 4 

while x > 0:
    print('SPAM!!! ' * x, x)
    x -= 1

"""

while x > 0:
    print('SPAM!!! ' * x, x)
    x -= 1

first iteration of while loop X -> 4 
next iteration of while loop X -> 3 
next iteration of while loop X -> 2
next iteration of while loop X -> 1
next iteration of while loop X -> 0 (this is where while loop ends because x is not greater than 0)


"""




    

# mapping denotes an object that maps keys to associated values, mapping do not maintain any left-to-right positional ordering, they support access to data stored by key, 