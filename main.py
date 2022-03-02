# Basics input
print("Input value 1")
inpnum = input()
print("Input value 2")
inpnum2 = input()
print("The sum is" ,int(inpnum)+int(inpnum2))

# Basic input and finding type
var1 = "Hello"
var2 = 2
var3 = 5
sum = var2 + var3
print("The sum is" ,sum)
print(type(var1))

# Data Structure - Dictionary
d1 = {}
print(type(d1)) # class dict
d2 = {"Adeel":"burger","ali":"samosa","ahmad":"water","murtaza":{"A":"val1","B":"val2","C":"val3"}}
print(d2["murtaza"]["B"]) # case sensitive
d2["obaid"] = "Kebab"
print(d2["obaid"])

# Excercise - Dictionary
d1 = {"A" : "val1","B": "val2","C": "val3",
        "D": "val4","E": "val5",}
print("Pick from A to E")
vinp = input()
print(d1[vinp])

## Data Structure - Sets
s = set()
print(type(s))

s_from_list = set([1,2,3,4])
print(type(s_from_list))
s.add(2)
s1 = s.union((3,4))
print(s,s1)

## Conditions
var1 = 5
var2 = 60
var3 = int(input())
if var3 > var2:
    print("Greater")
elif var3 == var2:
    print("Equal")
else:
    print("Lesser")

##
list = [1,2,3,4]
if 4 in list:
    print("Yes its there")

# Excercise - Faulty Calculator
num1 = int(input("Input first value : "))
op = input("Choose one : +, -, *, /, ** : ")
num2 = int(input("Input second value : "))

if num1 == 45 and num2 == 3 and op is "+":
    ans = 555
    print("Your answer is ", ans )
elif num1 == 65 and num2 == 6 and op is "/":
    ans = 4
    print("Your answer is ", ans )
elif num1 == 65 and num2 == 9 and op is "+":
    ans = 77
    print("Your answer is ", ans )        
elif op is "+":
    ans = num1+num2
    print("Your answer is ", ans )
elif op is "-":
    ans = num1-num2
    print("Your answer is ", ans )
elif op is "*":
    ans = num1*num2
    print("Your answer is ", ans )
elif op is "/":
    ans = num1/num2
    print("Your answer is ", ans )
elif op is "** ":
    ans = num1 ** num2
    print("Your answer is ", ans )
else:
    print("Error! Contact us" )


## Loops - For loop
list1 = [int,float,1,2,3,4,5,6,7,8,9,"hello","hi","65"]
list2 = ["a", "b", "c", "d"]
for item in list1:
    if str(item).isnumeric() and int(item)>6: 
        print(item)

##
i=0
while(i<45):
	print(i)
	i = i+1

## if you want to the condition inside    
i = 0
while(True):
    if i + 1 < 5:
        i = i + 1
        continue
    print(i+1, end=" ")
    if i==20:
        i = i + 1
        break
    i = i + 1


## Quiz
while(True):
    inp = int(input("Enter int value : "))
    if inp < 100:
        print("Try again with another integer")
        continue
    else:
        print("Congrats")
        break        

##
# Arithmetic Operators
print("5 + 6 is ", 5+6)
print("5 - 6 is ", 5-6)
print("5 * 6 is ", 5*6)
print("5 / 6 is ", 5/6)
print("5 ** 3 is ", 5**3)
print("5 % 5 is ", 5%5)
print("15 // 6 is ", 15//6)

# Assignment Operators
print("Assignment Operators")
x = 5
print(x)
x %=7 # x = x%7
x +=5
print(x)

# Comparison Operators
i = 5


# Logical Operators
a = True
b = False

# Identity Operators
print(5 is not 5)

# Membership Operators
list = [3, 3,2, 2,39, 33, 35,32]
print(324 not in list)

# Bitwise Operators - Binary value
0 - 00
# 1 - 01
2 - 10
3 - 11

print(0 & 2)
print(0 | 3)

##
# custom Functions and doc string
a = 2
b = 5
c = sum((a,b)) # built in function

def func1(a,b):
    print("You are in func1", a+b)

def func2(a,b):
    ''' This is docstring demo, you can use doc string'''
    average = (a+b)/2
    print(average)
    return average

print(func2(4,6))
print(func2.__doc__) # to print doc string of function

##
# Try except is try catch in java | Exception Handling
# It will just catch the error in print e form and move on, it won't stop the program
print("Enter num 1")
num1 = input()
print("Enter num 2")
num2 = input()

try:
    print("The sum of this number is : ",num1 + num2)
except Exception as e:
    print(e)
print("anything")   

##
# file io basics
'''
"r" - open file for reading
"w" - open file for writing
"x" - create file if not exists
"a" - append, add more file to contents
"t" - text mode
"b" - binary mode 27.
'''

file = open("readme.md","rt")
content = file.read() # you can specify the character count as arg
content = file.readline() #it will take the newline character aswell to print new line
content = file.readlines() #it will put the line in list
# print(content)
# file.close()
for line in file: # read line by line, if you want character then iterate through content
    print(line)
print(content)
file.close()

##
# file writing and appending 
file = open("readme.md", "a") # "w" for writing,creating file
file.write("This file was edited by python program.")
a = file.write("This file was edited by python program.") # will return how many characters were appended
print(a) 
file.close()

##
# Read and write a file both
file = open("readme.md","r+") # read and write
print(file.read())
file.write("Add more into it.")

##
# more on file
file = open("readme.md" , "rt") # rt is already by default tho
print(file.readline())
print(file.tell()) # tell you where is file pointer
file.seek(0) # seek a pointer to a location
file.close() # always close the file

##
# How to open file with "with" 
with open("readme.md" , "rt") as file :
    content = file.read(4)
    print(content)

## you don't have to close file via this method
# global keyword will give you permission in local scope to read/write in local domain , it won't work in nested scopes, when you type global it just straight go out of the nested scope to global top
x = 89
def func1():
    x = 20
    def func2():
        global x
        x = 8
    func2() # it won't change the value of x in func 2, if none found, it will create in global
func1()
print(x) # will print 8 and will create global variable if not created at top

##
# Recursion
# Factorial 
def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
    

number = int(input("Enter the number : "))
print("Factorial using recursive method : " , factorial_recursive(number))
print("Factorial using recursive method : " , factorial_iterative(number))

# Fibonacci series
# 0 1 1 2 3 5 8 13
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    

number2 = int(input("Enter the number for fib : "))
print("Fibonacci : " , fib(number2))

##
# Lambda Function or Anonymous Functions , its just a short version of funtion
def add(a,b):
     return a+b
add2 = lambda a,b: a+b

print(add(2,3))
print(add2(2,3))

def a_first(a):
    return a[1] # sort with 1 index
a = [[9,4],[5,6],[2,3]]
# a.sort(key = a_first) # key take functions
a.sort(key = lambda a : a[1]) #or you can just use this
print(a)

##
# Using modules, you can install other module using pip install e.g sklearn etc
from ast import Add
import random
rand = random.randint(0,5)
print(rand)
list = list(('apple', 'banana', 'cherry'))
print(random.choice(list))

##
# F Strings - to format the string
import math
a = "edie"
b = 5
line = "this is %s %s"%(a,b)
line = "this is {1}{0}"
form = line.format(a,b)
print(form)
# or
c = f" This is {a} {b} {4+8}{math.cos(5)}"
print(c)

##
# Args and kwargs - to use list or string as parameter
def funargs(x,*args,**kwargs): # args and kwargs is just a conventional words
    print(x)
    print(type(args))
    print(args[0])
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key} is the {value}")

list = ["a","b","c","d"] # this list will go as a tuple in args
normal = "this is the normal argument"
kw = {"a":"1","b":"2"}
funargs(normal,*list,**kw)

##
# Time module
import time

initial = time.time()
print(initial)
k=0
while k<10:
    print("This is Adeel")
    k+=1
print("While loop ran for ", time.time() - initial)    
initial2 = time.time()
for i in range(10):
    print("This is Adeel") 
print("For loop ran for ", time.time() - initial2)    

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

##
# Enumerate Function
list = ["A","B","C","D","E"]
i = 0
for item in list:
    if i % 2 == 0:
        print(item)
    i+=1
# Enumerate will return index along with item
for index,item in enumerate(list):
    if index % 2 == 0:
        print(f"Please buy {item}")

##
# We use  __name__ == '__main__' when we import another file, so we want to run all the code except some line of code. So we put the code in __main__ which we dont want to run
# Content of test.py file below.
def printstr(string):
    return f"This is string {string}"
def add(num1, num2):
    return num1 + num2 + 2

if __name__ == '__main__':
    print("hi")
    o = add(4,6)
    print(o)

# so in main file importing
# import test.py
# print(test.add(4,2)) # so it will import the other file, and run all except the code in __main__

##
# Join function
list =["John", "b", "c", "d","w"]
for item in list:
    print(item, "and",end=" ")
# you can do above by below code
a = "and ".join(list)
print(a)

##
# Map Function allow you to apply another function on all the element
func2 = [2,3,6,5,8,4,6,33,56]
for i in func2:
    print(i)
for i in range(len(func2)):
    print(func2[i])   
    #or use map
numbersInStrings = ["33", "55", "49", "67"]
numbersInInt = list(map(int, numbersInStrings))
print(numbersInInt[2]+3)
# built in function
num = [2,3,6,5,8,4,6,33,56]
square = list(map(lambda x:x*x,num))
print(square)

# another example
def square(x):
    return x*x
def cube(x):
    return x*x*x
func = [square,cube]
func2 = [2,3,6,5,8,4,6,33,56]

for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)
for i in range(len(func2)):
    val = list(map(lambda x:x(i),func))
    print(val)

##
# Filter Function it will return true
list_1 = [1,2,3,4,5,6,7,8,9]
def is_greater_than(x):
    return x>5
greater_than_5 = list(filter(is_greater_than, list_1))
print(greater_than_5)

##
# Reduce function
from functools import reduce
list1 = [1,2,3,4,5]
num = 0
for i in list1:
    num = num + i
print(num)
    # or use reduce function
num = reduce(lambda x,y:x+y, list1)
print(num)

##
# Decorator is kinda blueprint, a premade template to run lil bit change functions
def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1
def test():
    print("Hello")
# test = dec1(test) == @dec1 are basically same thing
test()

##
# Generators - are iterator which can iterate once
# Generator function are function in which we can yield, mean it capable to generate but not generating
'''
Iterable - ___item___() or __getitem___()
Iterator - __next__() 
Iteration
'''
def gen(n):
    for i in range(n):
        yield i #to make it capable but not yet run, validate that it can run.

g = gen(3)
print(g)
print(g.__next__())
print(g.__next__())
print(g.__next__())
# or 
for i in g:
    print(i) # for loop auto handle the stop iteration

h = 1234 # integer is not iterable
a = "adeel"
for c in a:
    print(c) # string is iterable

##
# Comprehension - list, dict, set, generator comprehension
ls = []
for i in range(100):
    if i%3==0:
        ls.append(i)

ls = [i for i in range(100) if i%3==0]
print(ls)

## Dictionary comprehension
# if you want to auto fill dict
# dict = {0: "item0", 1 : "item1" and so on}
dict = {    i:f"item{i}" for i in range(1000) if i % 100==0}
dict = {    i:f"Item{i}" for i in range(5)}
# to reverse your dictionary
dict2 = {value:key for key, value in dict.items()}
print(dict,"\n",dict2)

### set comprehension
dresses = {dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2"]}
print(dresses)

### Generator comprehension use parenthesis
evens = (i for i in range(100) if i%2==0)
print(evens.__next__()) 
print(evens.__next__()) 
# or 
for item in evens:
    print(item)

##   
# Using else with For loops
list = ["a","b","c"]
for item in list:
    print(item)
    break
else: # if you want to print something when for loop is ended properly
    print("For loop ended")
for item in list:
    if item == "d":
        break   
else: 
    print("Your item was not found")

##
# Function Caching
import time
from functools import lru_cache

# lru is a decorator which allow cache upto 3 value. So it will cache the same call.
@lru_cache(maxsize=3)
def some_work(n):
    # Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    print("Done..Calling again")
    some_work(3)
    print("Called again")

##
# Else and Finally in try except
file = open("readme.md")
try:
    file1 = open("doesnotexist.txt")
except IOError as e:
    print("We got an IOError",e)
except EOFError as e:
    print("We got an EOFError",e)
else: # only except or else will run
    print("This will run only if except is not runnig")    
finally: # as the name suggest it will run in all condition
    # we use finally for code cleanup
    print("Run this code anyway")
    file.close()
    
##
# Coroutines - lets you use your function from the middle, you don't have to run all the coroutine from the top
def searcher():
    import time
    book = "A quick brown fox jumps"
    time.sleep(4) # time consuming task

    while True:
        text = (yield)
        if text in book:
            print("The text is in book")
        else:
            print("The text is not in the book")

search = searcher()
next(search) # this line run the code snippet before while loop
search.send("Okay") # this line will go directly to while true, text = (yield)
input("press any key")
search.send("Okay and")
search.close() # We close coroutine just like closing the file 

##
# OS Module - to interact with os
import os 
# print(dir(os)) # what can you do with os module
print(os.getcwd())
print(os.listdir())
print(os.environ.get("Path"))
print(os.path.join("C://", "/Path")) # join path in optimal way
print(os.path.exists("C://"))
print(os.path.isdir("C://"))

##
# Request Module GET/POST Request
import requests
# r = requests.get("https://anime-facts-rest-api.herokuapp.com/api/v1")
r = requests.get("https://anime-facts-rest-api.herokuapp.com/api/v1/fma_brotherhood/2")
print(r.text)
print(r.status_code) # 200 is okay

url = "www.something.com"
data_dict = {"p1",4,"p2",2}
r2 = requests.post(url=url, data=data_dict)
# OR Use postman and create payload via Code snippet
url = "http://httpbin.org/post"
payload={'test1': 'value1','test2': 'value2'}
files=[]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)

##
# Json module
import json
data = '{"var1":"val1","var2":23}'
# loads convert string to JSON
parsed = json.loads(data)
print(parsed)

data2 = {
    "var1 ": "value1",
    "var2" : ["a",'b',"c","d"],
    "var3" : ('q','w','e'),
    "isbad" : False
}
# dumps make code js compatible, make it as json object
jscomp = json.dumps(data2)
print(jscomp)

##
# Pickle Module - to pack and unpack any object
import pickle
# Pickling a python object into a file
list = ["a","b","c","d","e"] # the value can be list of objects
file = "mylist.pkl"
fileobj = open(file,'wb') # write binary
pickle.dump(list,fileobj)
fileobj.close()

# to depickle
file = mylist.pkl
fileobj = open(file,r)
mylist = pickle.load(fileobj)
print(mylist)
print(type(mylist))
# what is pickle.loads? <- 
##
