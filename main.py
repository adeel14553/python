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


## Loops
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

## Excercise - Guess the number game?
