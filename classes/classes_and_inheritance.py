"""
CLASSES ARE CUSTOMIZED BY INHERITANCE

Superclasses are listed in parentheses in a class header
- to make a class inherit attributes from another class, just list the other class in parentheses in the new class statement's header
    - the class that inherits is usually called a SUBCLASS and the class that is inherited from is its SUPERCLASS

- classes inherit attributes from their superclasses

- instances inherit attributes from all accessible classes 
    - each instance gets names from the class it is generated from
        - when looking for a name, Py checks the instance, then its class, then all superclasses 

- each object.attribute reference invoke a new, independent search 

- logic changes are made by subclassing, not by changing superclasses 

"""

import polymorph_and_classes
from polymorph_and_classes import FirstClass

class SecondClass(FirstClass):                      # inherits first class
    def display(self):                              # changes display
        print('Current value = "%s"' % self.data)


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self): 
        return '[ThirdClass: %s]' % self.data
    def mul(self, other):
        self.data *= other

a = ThirdClass('abc')
a.display()
print(a)

b = a + 'xyz'
b.display()
print(b)

a.mul(3)
print(a)