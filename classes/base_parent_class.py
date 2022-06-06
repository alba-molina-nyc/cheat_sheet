class Animal:                       #this is the base or parentclass
    def eat(self):                  #defines method
        print("I can eat")

class Dog(Animal):                  #derive dog class from animal class passes in Animal
    def bark(self):                 #bark method passed into Dog class that is specific to the dog class
        print("i can bark")

class Cat(Animal):
    def meow(self):
        print("i can meow")

dog1 = Dog()                        # create new object of the Dog Class
dog1.bark()                         # the object(dog1) has access to the bark method
dog1.eat()                          # the object has access to the eat method


"""
more practical method
write a parent class called polygon
then write two derivaritive classes one for triangle and one for quadrilateral that derives from the parent polygon class
"""