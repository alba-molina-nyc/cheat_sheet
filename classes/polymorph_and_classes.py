"""
CLASSES
* you can tell a method from a function because a method will always pass in "self" and a regular function will not 


class FirstClass:                                                       # define a class object
    def setdata(self, value):                                           # define a class' method
        self.data = value                                               # self is the instance
    def display(self):
        print(self.data)                                                # self.data per instance



CLASS OBJECTS PROVIDE BEHAVIOR 
- the class statement creates a class object and assigns it a name. 
    - It is an executable statement 
    - when reached and run, it generates a new class object and assigns it to the name in the class header

- assignments inside class statements make class attributes
    - the class statement defines a local scope that morphs into the attribute namespace of the class object
    - after running a class statement, class attributes are accessed by name qualification 
        - object.name

- class attributes provide object with STATE and BEHAVIOR 
    - attributes of a class object record state info and behavior to be shared by all instances created from the class
    - function def statements nested inside a class generate a method, which process instances 

INSTANCE OBJECTS ARE CONCRETE ITEMS
- calling class object like a function makes a new instance object
    - each time a class is called it creates and returns a new instance object 
    - instances represent concrete items in your program's domain

- each instance object inherits class attributes and gets its own namespace
    - instance objects created from classes are new namespaces, they start empty but inherit attributes that live in the class objects from which they were generated

- assignments to attributes of self in methods make per-instance attributes 
    - inside a class' method functions, the first argument (called self) references the instance object being processed
    - assignments to attributes of self create or change data in the instance not the class 

"""

class FirstClass:
    def setdata(self, value):
        self.data = value 
    def display(self):
        print(self.data)

x = FirstClass()                                    # making class instances
y = FirstClass()

x.setdata("Victoria Molina")
y.setdata("Alba Molina")