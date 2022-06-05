import core_data_types.matrix as matrix
from core_data_types.matrix import M


"""
list comprehension expressions - are a powerful way to proecess structures like our matrix
bc it is easy to grab rows by simple indexing because the matrix is stored by rows



"""

col2 = [row[1] for row in M] # collect the items in column 2 
print(col2)

print(M)

x = [row[1] + 1 for row in M] # add 1 to each item in column 2
"""

before adding 1 to column 2 


[       c2
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]


"""
print(x)

"""
collect a diagnal from a matrix
"""

print(M)

diag = [M[i][i] for i in [0,1,2]] # collect diagnal 
print(diag)

doubles = [c*2 for c in 'spam'] # doubles AKA repeat characters in strings
print(doubles)

doubles_matrix = [[i]*2 for i in M]
print(doubles_matrix)