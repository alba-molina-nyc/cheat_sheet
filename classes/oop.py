"""
why OOP

imagine you need to create a program that 
1. takes student name
2. based on student name determines if they passed or failed

step 1 define the class 

whenever you define methods you need to pass "self" first as the first argument, in this case self represents student1
if you create another object then self represents that object

whenever __init__ is passed it defines and immediately calls on the attributes 
"""

class Student:                        # defines class
    def check_pass_fail(self):        # define method aka function
        if self.marks >= 40:
            return True
        else:
            return False
    
    def __init__(self, name, marks):                # init is a method used to instantiate attributes aka variables for classes
        self.name = name
        self.marks = marks

student1=Student("Marc", 85)
student2=Student("Janet", 30)

print(student1.marks)
print(student2.name)                # printing attributes

did_pass = student1.check_pass_fail()
print(did_pass)
did_pass = student2.check_pass_fail()
print(did_pass)



did_pass = student1.check_pass_fail()
print(did_pass)