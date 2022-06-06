"""write a function firstlast that takes a sequence (string, list, tuple) and returns the first and last elements of that sequence.

str = "abdefg"
return ag

lst = [1,2,3,4,5,6]
return 1,6


"""

from pyparsing import stringStart


def firstlast(items):
    first = ''
    last = ''
    len_counter = 0

    while items != None: 
        for i,v in enumerate(items):
            first = items[0]
            # [-1] aka negative indexings
            last = items [- 1]
            len_counter += 1
        print("first", "==>",first, "last=>" ,last)

        break
    return first, last


            

firstlast('vickygarafola')
firstlast([9,1,2,3,4])
firstlast([(1,2),(24,25),('yes', 'hell yes')])


# firstlast('12345')

#   for item in items:
#         print(item, 'appears @ =>', len_counter)
#         len_counter += 1



