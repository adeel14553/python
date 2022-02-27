# Class - Template
# Object - Instance of the Class
# Works on the concept of DRY - Do not repeat Yourself

##
# 
class Student:
    pass # when you don't want to use anything use "pass"

adeel = Student()
edie = Student()
adeel.name = "Adeel"
edie.name = "edie"
print(adeel.name, edie.name)

##
# Instance and Class Variable
class Employee:
    no_of_leaves = 8
    pass

edie = Employee()
ali = Employee()

edie.name = "Edie"
edie.salary = 40
edie.role = "Student"
ali.name = "Ali"
ali.salary = 50
ali.role = "Student"
edie.no_of_leaves = 10 # Instance Variable
Employee.no_of_leaves = 12 # Class Variable
print(edie.__dict__)
print(Employee.no_of_leaves,edie.no_of_leaves)

##
# Self and init Constructor
class Employee:
    no_of_leaves = 8
    def __init__(self, cname, csalary):
        self.name = cname # self.name is instance variable
        self.salary = csalary

    def printdetails(self): #self is that object to which this method is applied on, is called with obj, e.g edie, ali , see line 52 print(edie.printdetails())
        return f"Name is {self.name}. Salary is {self.salary}" # f string

edie = Employee("Edie",40) # to give arguments to class, we use constructor and __init__, the argument goes into __init__
ali = Employee("Ali",50)
edie.no_of_leaves = 10 # Instance Variable
Employee.no_of_leaves = 12 # Class Variable

print(edie.printdetails()) # edie will be taken as argument in the function printdetails as self

##
# Class Method
class Employee:
    no_of_leaves = 8
    def __init__(self, cname, csalary):
        self.name = cname # self.name is instance variable
        self.salary = csalary

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}" # f string

    @classmethod
    def change_leaves(cls, newleaves): # cls is class itself, Employee
        cls.no_of_leaves = newleaves #temp change in class variable

edie = Employee("Edie",40) # to give arguments to class, we use constructor and __init__, the argument goes into __init__
ali = Employee("Ali",50)
edie.no_of_leaves = 10 # Instance Variable
Employee.no_of_leaves = 12 # Class Variable
edie.change_leaves(30) # it will change class variable not instance variable

print(Employee.no_of_leaves)

##
# Class Method as Alternate Constructor
class Employee:
    no_of_leaves = 8
    def __init__(self, cname, csalary):
        self.name = cname # 
        self.salary = csalary

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}" 

    @classmethod
    def change_leaves(cls, newleaves): 
        cls.no_of_leaves = newleaves 
    @classmethod
    def from_dash(cls,string):
        # params = string.split("-") # return list
        # print(params)
        # return cls(params[0],params[1])
        # or one liner below
        return cls(*string.split("-")) # args and kwargs

edie = Employee("Edie",40) 
ali = Employee("Ali",50)
guy = Employee.from_dash("Karan-30") # used as alternate constructor


edie.change_leaves(51)

print(Employee.no_of_leaves)
print(guy.salary)

##
# Static Method - @staticmethod created as decorator, behave like it is not inside a class, but it is, you can use it with instances
class Employee:
    no_of_leaves = 8
    def __init__(self, cname, csalary):
        self.name = cname # 
        self.salary = csalary

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}" 

    @classmethod
    def change_leaves(cls, newleaves): 
        cls.no_of_leaves = newleaves 
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-")) 
    
    @staticmethod
    def printgood(string):
        print("This is good " + string)

edie = Employee("Edie",40) 
ali = Employee("Ali",50)
guy = Employee.from_dash("Karan-30") 

edie.change_leaves(51)

# print(guy.printgood("Guy")) # will return status code, if none , none will be returned
guy.printgood("Guy")
print(Employee.no_of_leaves)
print(guy.salary)

##
# Abstraction and Encapsulation 
# One component is a layer of abstraction, to achieve abstraction we use encapsulation, encapsulation mean to hide details
# Encapsulation tells you what it does not how it does

## 
# Inheritance
# Abstraction and Encapsulation 
# One component is a layer of abstraction, to achieve abstraction we use encapsulation, encapsulation mean to hide details
# Encapsulation tells you what it does not how it does
class Employee:
    no_of_leaves = 8
    def __init__(self, cname, csalary):
        self.name = cname
        self.salary = csalary

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}" 

    @classmethod
    def change_leaves(cls, newleaves): 
        cls.no_of_leaves = newleaves 
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-")) 
    
    @staticmethod
    def printgood(string):
        print("This is good " + string)

edie = Employee("Edie",40) 
ali = Employee("Ali",50)
guy = Employee.from_dash("Karan-30") 

# Inheritance
class Programmer(Employee):
    no_of_holiday = 20
    def __init__(self, cname, csalary, clanguage):
        self.name = cname
        self.salary = csalary
        self.languages = clanguage

    def printprog(self):
        return f"Programer name is {self.name} and know {self.languages}"

max = Programmer("Max",60,["Python"])
dan = Programmer("Dan",70,["Java"])


edie.change_leaves(51)

# print(guy.printgood("Guy")) # will return status code, if none , none will be returned
guy.printgood("Guy")
print(Employee.no_of_leaves)
print(guy.salary)
print(dan.printprog())
print(dan.printdetails())

##
# Multiple Inheritance
class Employee:
    no_of_leaves = 8
    def __init__(self, cname, csalary):
        self.name = cname
        self.salary = csalary

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}" 

    @classmethod
    def change_leaves(cls, newleaves): 
        cls.no_of_leaves = newleaves 
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-")) 
    
    @staticmethod
    def printgood(string):
        print("This is good " + string)

class Player():
    no_of_games = 4
    def __init__(self,name,game):
        self.name = name
        self.game = game
    
    def printdetails(self):
        return f"The name is {self.name} has played {self.game} games"

class CoolProgrammer(Employee, Player): # order is important
    language = "Cpp"
    def printLanguage(self):
        print(self.language)
    pass

edie = Employee("Edie",40) 
ali = Employee("Ali",50)
guy = Employee.from_dash("Guy-30") 
jack = Player("Jack", ["Cricket"])
reacher = CoolProgrammer("Reacher", 500)
print(reacher.printdetails())
reacher.printLanguage()

##
# Multilevel Inheritance 
class Dad():
    basketball = 1
    pass
class Son(Dad):
    running = 1
    def isrunning(self):
        return f"Yes i am running {self.running}"
    pass
class Grandson(Son):
    running = 5
    def isrunning(self):
        return f"Yes i am running very fast {self.running}"
    pass

a = Dad()
b = Son()
c = Grandson()

print(c.isrunning())
print(c.basketball) # will look in itself then in Son then in Dad

##
# Public,private, protected variables - Public share with all, protected share with siblings, private share with me only, family analogy
class A:
    var = 10
    _protected = 20
    __private = 50 

instance = A()
print(instance._protected)
print(instance._A__private) # name mangling, you can use it like that

# Polymorphism - ability to take various forms
# To take multiple form, e.g two class inherited and you override one function, so it like version 2.0

##
# Overridding

class A:
    classvar1 = "I am class var in class A"
    def __init__(self):
        self.var1 = "I am in class A constructor"
        self.classvar1 = "Instance var in class A constructor"
        self.special = "Special"
class B(A):
    classvar1 = "I am in class B"
    def __init__(self): # now that class a contstructor is overriden it won't run, if you still want to run it then use this below line
        super().__init__()
        self.var1 = "I am in class B constructor"
        self.classvar1 = "Instance var in class B constructor"
a = A()
b = B()

print(b.classvar1) # It will first look for instance variable, then parent class variable
print(b.special) # accessed via super coz constructor was overriden 

##
# Diaomond shape problem due to multiple inheritance
class A:
    def met(self):
        print("Method from Class A")
class B(A):
    def met(self):
        print("Method from Class B")
class C(A):
    def met(self):
        print("Method from Class B")
class D(B,C):
    pass


a = A()
b = B()
c = C()
d = D()

d.met() # it will first check in B,then C if not found in itself

##
# Operator overloading and dunder method are those which start or end with __
class Employee:
    no_of_leaves = 8

    def __init__(self, cname, csalary):
        self.name = cname 
        self.salary = csalary

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}" 

    @classmethod
    def change_leaves(cls, newleaves): 
        cls.no_of_leaves = newleaves 

    def __add__(self,other): # dunder method 
        return self.salary + other.salary
    
    def __repr__(self): # dunder method 
        return f"Employee('{self.name}',{self.salary})"
    def __str__(self): # dunder method 
        return f"Name is {self.name}. Salary is {self.salary}" 
    
emp1 = Employee("John", 250)
emp2 = Employee("Ali", 95)

print(emp1 + emp2)
# if str is available then str will run, if not then repr will be used. priority is str>repr
print(str(emp1))

##
# Abstract Base Class
# from abc import ABCMeta, abstractmethod
# or use below
from abc import ABC, abstractmethod
# you can't make object of abstract base class
class Shape(ABC):
# class Shape(metaclass = ABCMeta):
    @abstractmethod # means everyone should define this method, if child don't have abstract method printarea it will throw error
    def printarea(self):
        return 0

class Rectangle(Shape): 
    type = "rectangle"
    sides = 4
    
    # Constructor
    def __init__(self):
        self.length = 6
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect = Rectangle()
print(rect.printarea())

##
# Setters and property decorator
class Employee:
    def __init__(self,fname,lname) -> None:
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This Employee is {self.fname} {self.lname}"
    
    @property # property decorator , to run lil bit change functions
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"
    
    @email.setter # extracting names from email via setters
    def email(self,string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]    

    @email.deleter
    def email(self):
        self.lname = None
        self.fname = None

ma = Employee("Muhammad","Adeel")
ef = Employee("Ed", "Felix")

print(ma.explain())
print(ma.email)
ma.fname = "Ahmad"
print(ma.email)
ma.email = "Gul.Ahmad@biz.com"
print(ma.email)
del ma.email # handle via property decorator
print(ma.email)

##
# Object Introspection - To inspect more about object
class Employee:
    def __init__(self,fname,lname) -> None:
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This Employee is {self.fname} {self.lname}"
    
    @property # property decorator , to run lil bit change functions
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"
    
    @email.setter # extracting names from email via setters
    def email(self,string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]    

    @email.deleter
    def email(self):
        self.lname = None
        self.fname = None

john = Employee("John", "Player")
print(john.email)
# ways of inspection
print(type(john))
print(id(john))
print(dir(john)) # dir will let you what you can do with that object
import inspect
print(inspect.getmembers(john))
