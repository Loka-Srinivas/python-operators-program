# rahul folder
# date="2025-09-15"
#-------------------------------------------------------------
# method overridding
# class Animal:
#     def speak(self):
#         print("animals are make sounds")
# class Dog(Animal):
#     def speak(self):
#         print("dogs are barking")
# dog1=Dog()
# dog1.speak()
#-----------------------------------------------------------------

#operater overloading:-


# class Book:
#     def __init__(self,pages):
#         self.pages=pages
#     def __add__(self,other):
#         return self.pages+other.pages
#     def __mul__(self,other):
#         return self.pages*other.pages
#     def __sub__(self,other):
#         return self.pages-other.pages
# b1=Book(100)
# b2=Book(200)
# print(b1+b2)
# print(b1*b2)
# print(b1-b2)
#-------------------------------------------------------------------

#abstraction in oops:-



# def:hide the unnessasari details and show only the required futures to the user.
# here we use the buld in class and a method to implement the  abstraction in our program.
#we declare a classs as abstract by inheriting the ABC calss into the class
#we ant create the obj for an abstract  by inheriting th ABC class into that class
#we wont define a method in abstract class we just a declare it.

#we define at the abstrct method in the normaml classses where the 
#ABC stands for abstarct base class.
 
#we declaring the metho as abstract we ensure that method is defined in all the sub classes below it 


# from abc import ABC,abstractmethod   #impoeted abs and abstractmethod
# class Vehicle(ABC): #abstarctv class declaration
#     @abstractmethod  # @ means decorater -in order to declare a method as abstract method
    
#     def milage(self):  # abstract method declaration
#         pass

# # v=Vehicle()
# # v.milage  # gives an error
# class Tesla(Vehicle):
#     def milage(self):
#         print("the milage is 300km for tesla")
# t1=Tesla()
# t1.milage()


# from abc import ABC,abstractmethod
# class jwellery(ABC):
#     @abstractmethod
#     def carats(self):
#         pass
# class gold(jwellery):
#     def carats(self):
#         print("gold has highest at the 22 carats gold")
# class gold1(jwellery):
#     def carats(self):
#         print("this is 24 cararts gold biscates")
#     def type(self):
#         print("gold method is naclace")
# g1=gold()
# g2=gold1()
# g1.carats()
# g2.carats()
# g2.type()



# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     def info(self):
#         print("This one is considered asa shape")
        
# class Rectangle(Shape):
#     def __init__ (self, length, breadth):
#         self.length=length
#         self.breadth=breadth  
        
#     def area(self):
#         return self.length*self.breadth
    
# rect=Rectangle(10,5)
# rect.info()  
# print("The area of a rectangle:",rect.area())         



# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Perimeter(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass

#     def info(self):
#         print("This one is considered as a shape")

# class Rectangle(Shape, Perimeter):
#     def _init_(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth

#     def perimeter(self):
#         return 2 * (self.length + self.breadth)

# # Object creation
# rect = Rectangle(10, 5)
# rect.info()
# print("The area of a rectangle:", rect.area())
# print("The perimeter of a rectangle:", rect.perimeter())





from abc import ABC, abstractmethod 

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Perimeter(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    def info(self):
        print("This one is considered as a shape")


class Rectangle(Shape, Perimeter):
    def __init__(self, length, breadth):   # fixed here
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


# Object creation
rect = Rectangle(10, 5)
rect.info()
print("The area of a rectangle:", rect.area())
print("The perimeter of a rectangle:", rect.perimeter())
