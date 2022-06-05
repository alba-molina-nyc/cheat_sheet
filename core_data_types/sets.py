# """
# a sequence is a positionally ordered collection of items and you can refer to any item in the sequence by using its index number e.g. s[0]

# more on p.126
# """
# x = set('spam') # make a set out of a sequence
# # print(x)
# y = {'h', 'a', 'm'}
# print(x,y)

# print(x&y, 'intersection') # intersection

# print(x|y, 'union') #union

# print(x-y, 'difference') # difference
# print(x>y, 'superset') #superset

# print( {n ** 2 for n in [1,2,3,4]}, ' this is a set comprehension') # superset

# x = {n ** 2 for n in [1,2,3,4]}
# print(x) # you can assign it to a variable 

# """
# Sets are commonly used for filtering out duplicates, isolating differences, and performing order-neutral equality tests without sorting in lists, strings and all other iterable objects

# """

# print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham']) # seeing if something exists in a string and a list

# print(1 in [1,2,3,4]) # seeing if a number exists in a list


# /////

print(set('spam') - set('ham')) #finding differences in collection

print(set('spam') == set('asmp')) #order neutral equality meaning do they consist of the same thing
