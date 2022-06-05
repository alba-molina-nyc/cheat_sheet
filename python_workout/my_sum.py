# create a function that adds a number of arguments passed in
# empty list that will collect the numbers
# initialize first variable to zero, this is going to change as you iterate

# adds two nums

# def add_numbers(a,b):
#     return a + b

# x = add_numbers(4,4)
# print(x)

def get_nums(*nums):
    counter = 0
    list = []
    for n in nums: 
        if n != None:
            counter = counter + n
            print(counter, 'counter')
            list.append(counter)
            print(list, 'listsdfsd')
            continue
       

print(get_nums(100, 100, 23, 56, 1, 0 ), 'fuc')






