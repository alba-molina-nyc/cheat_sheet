"""
file objects 
can be used to read and write text memos, audio clips, excel docs, saved email messages and whatever else you happen to have stored in your machine
"""

f = open('first_file_code.txt', 'w') # make a new file in output mode, the 'w' stands for write
f.write('lorem hello this is my first data.txt file file file file file file') # you can write a string of characters to the file 

f.write('here a re some more texts that I want to add to this file file file file file file file that i just created i am having such fun fun fun fun fun239849327w5r9372450972305')


f.write('here a re some more texts that I want to add to this file file file file file file file that i just created i am having such fun fun fun fun fun2308403284023')

f.close()


"""
you can find all the different methods that belong to the file by running : 
print(dir(f))
"""
print(dir(f))

print(f.name)

