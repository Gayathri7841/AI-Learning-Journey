#Arithmetic Operators
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#Assignment operators

x=5
x+=5
print(x)
x-=5
print(x)
x*=5
print(x)
x/=5
print(x)
x%=5
print(x)
x//=5
print(x)
x**=3
print(x)
x=10
x &= 3
print(x)
x |= 3
print(x)
x ^= 3
print(x)
x >>= 3
print(x)
x <<= 3
print(x)
print(x := 3)

#ternary operators
age=14
x="can vote" if age>18 else "cannot vote"

#comparison operators
x=10
y=20
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#logical operators

x=20
print(x>=0 and x<=35)

print(x>5 or x<10)
print(not(x>=0 and x<=35))

#identity operators
x=[10 ,20 ,30]
y=[10,20,30]
z=x
print(x is y)
print(x is z) # can use is not operator also
print(x==y)


#membership operators
a=[10,20,30,80,75,63,49]
print(55 in a)#can use not in also


#bitwise operators
print(3&4)
print(3|4)
print(3^4)
print(~3)
print(3<<4)
print(3>>4)





