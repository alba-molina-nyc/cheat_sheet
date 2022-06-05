import core_data_types.lists as lists, core_data_types.matrix as matrix
from core_data_types.matrix import M


G = (sum(row) for row in M)


print(next(G), 'nxtG')
print(next(G), 'nxtG')