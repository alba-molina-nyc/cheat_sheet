"""
🔆 for loops can be used in lists
"""
"""
bc they are sequences, lists support all the sequence operations that strings does, the only difference is that the results are usually lists instead of strings
"""

L = [123, 'spam', 1.23]
len_method_list = len(L)
print(len_method_list)

L.append('NI')

print(L)

M = ['bb', 'aa', 'zz', 'cc']
print(M, 'before sorting')

M.sort() # sorting list
print(M)

M.reverse()
print(M) # reverse a list 

"""
range: from 0 -> number_selected - 1
in this case: 
0-12 AKA 11 
"""


def set_range__of_list(i): # i created this function myself
    LL = range(i)
    for i in LL: 
        print(i, 'iiiiii')

set_range__of_list(12)


rrr = [[x ** 2, x ** 3] for x in range(12)]
print(rrr)

# a sequence is a positionally ordered collection of objects, strings, lists and tuples are all sequences in python. you can index, concatenate, slice them
  

