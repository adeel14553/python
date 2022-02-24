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

    def printdetails(self):
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
# Static Method - created as decorator, behave like it is not inside a class, but it is, you can use it with instances
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