s = "Spam" # ℹ️ set variable to a string
"""
🔆 for loops can be used in strings
"""
print(dir(str))
print(s) # ℹ️ print string


print(len(s)) # ℹ️ you can get the length of a string


print(s[0]) # ℹ️ you can index a string


print(s[-1]) # ℹ️ you can index backwards (last item from the end)


print(s[-2]) # ℹ️ second last item from end

print(s[1:3]) # ℹ️ this is slicing- slice s from offsets 1 through 2 (not 3)
# print(s[:1])
# print(s[1:]) 

"""
❌
# strings are immutable AKA they cannot be changed  

 s[0] = "x"

 You will get: 

 Traceback (most recent call last):
  File "/Users/albamolina/interviews/cheat_sheet/strings.py", line 24, in <module>
     s[0] = "x"
# TypeError: 'str' object does not support item assignment

❌

# """

# ℹ️ but you can run expressions to make new objects 
y = 'z' + s[1:] 
print(y)

"""

# strings have operations of their own known as methods - AKA functions attached to and act upon a specific object

# """

find_method = s.find('pa') # ℹ️ find the offset of a substring in s
print(find_method)

replace_method = s.replace('pa', 'ABC') # ℹ️ replace occurence in a string
print(replace_method)

line = 'aaa,bbb,ccccc,dd'
split_method = line.split(',') # ℹ️ split a delimiter into a list of substrings
print(split_method) 

upper_method = s.upper() # ℹ️ upper conversion
print(upper_method)

method_isalpha = s.isalpha() # ℹ️ content tetssl isalpha, isdigit etc.
print(method_isalpha)

liner = 'aaa,bbb,ccc,dd\n '
print(liner, 'liner')

method_r_strip = liner.rstrip() # ℹ️ remove whitespace characters on the right side
print(method_r_strip)
 
combine_two = liner.rstrip().split(',') # ℹ️ combine two operations
print(combine_two)


print(int('42') + 42) # string conversion


# p. 224 may be impt if comes up


string_ex = "s,pa,m"
print(string_ex)

find_mid = string_ex.__contains__('pa')

print(find_mid, 'sfsdf')
              
get_at = string_ex.find('pa')
print(get_at, 'here', string_ex)

"""
better way of find pa is to slice or split """

print(string_ex[2:4], "slice") #slice
print(string_ex.split(',')[1]) #split 


"""
TODO:
figure out how to remove spaces from strings and other unwanted characters

"""
charcount = "a\nb\x1f\000d"
print(len(charcount))