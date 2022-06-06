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
USES INHERITANCE


Polygon 
will have three methods __init__() 
get_perimeter()
display_info()

then it will have two derived classes: Trianle and Quadrilateral
in these classes we will add methods specific to them 
"""
"""
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter  
        
        this is the base class so all the other classes that derive from the polygon class will have these functions at the disposal"""

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter    


class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")
        """"but if you need you can write code like this to get the method from the parent class
        class_name.method_name(self)"""
        Polygon.display_info(self)
        """alternatively could also use a built in function that was built into the python language for this exact purpose"""
        super().display_info()


class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")


t1 = Triangle([5,6,7])                     # when create the t1 object the init method of the polygon class is called immediately      
perimeter = t1.get_perimeter()             # calls the get_perimeter method that is defined in the polygon class
# print("the perimeter is", perimeter)


"""METHOD OVERRIDING

if the same method is defined in both base and derived classes, then the method of the derived class overrides the method of the base class



call the method of the t1 triangle

but if you need we can call the method from the parent class """
t1.display_info()


q1 = Quadrilateral([5,6,7,8])
perimeter = q1.get_perimeter()




