#variables are ony create when u intialize them a value 
x=5
y=10
print(x)
print(y)
print(x+y)

#like in all other programming lang y will be updated
y="John"
print(y)

# type casting in python

x=str(9)
y=int(10)
z=float(13)
print(x)
print(y)
print(z)
print(y+z)
#print(x+y) # cannot add string and int,float,double or any other datatype

print(type(x))
print(type(y))
print(type(z))

#varible names are case sensitive

a=9
A=10
print(a)
print(A)

# a variable name can only start with either alphabet or underscore
#varibale name should only contain alphabets,numbers,underscore


#many values to multiple variables
x,y,z= 1,2,3
print(x,y,z)
x,y,z="orange",'biscuit',"hello"
print(x,y,z)

#one value to multiple variables

x=y=z="hii"
print(x,y,z)


#global variables
x="global"
def example():
    print("inside function",x)
example()
 

def example1():
    x=10
    print("inside the function",x);
example1()

print(x)

#to convert a local variable into a global variable 
def myfunc():
    global x
    x='fantastic'
myfunc()
print
