nrows = int(input("How many star lines you want : \n"))
bool = int(input("Input 1 or 0 : \n" ))

# Methond 1
for i in range(1,nrows+1):
    for j in range(1,i+1): 
        print(i, end=" ") 
    print()
for i in range(nrows,0,-1):
    for j in range(1,i+1):
        print(i, end=" ") 
    print()

# Method 2 
if bool == 0:
    for i in range(0,nrows+1):
        print("*"*i)
else:
    for i in range(nrows,0,-1):
        print("*"*i)    
    