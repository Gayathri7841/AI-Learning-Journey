#how to create sets?
set1={15,25,35,45,55,65,75}
#unordered,unchangeable,un indexed,no duplicates


#acessing set items
for x in set1:
    print(x)


#joining sets
set2={45,95,85,65,78,43,59,88,64,11}
set3={45,64,33,77,26,95,43,54,16,11}
set4=set2.union(set3)
print(set4)
#or
set5=set2|set3
print(set5)

set6=set2.update(set3)
print(set6)

set7=set2.intersection(set3)
print(set7)

set8=set2&set3
print(set8)

set9=set2.difference(set3)
print(set9)
set11=set2-set3
print(set11)
set10=set2.symmetric_difference(set3)
print(set10)

set12=set2^set3
print(set12)



