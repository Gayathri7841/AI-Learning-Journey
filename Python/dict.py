student1={
    "name":"rythm",
    "age":21,
    "id":1
    }

student2={
    "name":"eira",
    "age":22,
    "id":2
}
student3={
    "name":"arna",
    "age":22,
    "id":3
}

students={
    "student1":student1,
    "student2":student2,
    "student3":student3
}

print(student1['age'])
x=student2.get('age')
print(x)
y=student1.keys()
print(y)
z=student1.values()
print(z)
k=student1.items()
print(k)

student1['age']=25
print(student1['age'])

student1.update({"age":24})
print(student1['age'])

for x in student1:
    print(x)

for x in student1:
    print(student1[x])

for x in student1.values():
    print(x)
for x in student1.keys():
    print(x)
for x,y in student1.items():
    print(x,y)
    
