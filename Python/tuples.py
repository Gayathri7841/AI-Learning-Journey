#how to create tuples?
tuple8=(10,20,30,40,50,60)
#tuples are ordered , unchangeable, allows duplicates
print(tuple8)
#if want to create a tuple with one element u should use comma after the element
tuple1=(25,)
print(type(tuple1))#tuple

tuple2=(36)
print(type(tuple2))#int

#accessing tuples
print(tuple8[5])
print(tuple8[-3])
print(tuple8[2:5])
print(tuple8[:5])
print(tuple8[2:])
print(tuple8[-4:-1])
print(tuple8[-1:-4])


#changing tuples values
tuple1=(10,20,30,40)
y=list(tuple1)
y[2]=25
tuple1=tuple(y)
print(tuple1)
#same way can be used to add, delete,update values in the tuple

#unpacking tuples
(a,b,c,d,e,f)=tuple8
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
#or u can also write
(a,b,*c)=tuple8
print(a)
print(b)
print(c)
#or u can write
(a,b,*c,d)=tuple8
print(a)
print(b)
print(c)
print(d)


#looping in tuples
for x in tuple8:
    print(x)
#or 

for x in range(len(tuple8)):
    print(tuple8[x])
#or

while x<len(tuple8):
    print(tuple8[x])
    x=x+1

#joining tuples
t1=(10,20)
t2=(30,40)
t3=t1+t2
print(t3)

t1=t1*2
print(t1)
