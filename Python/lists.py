list=[10,20,30,40,50,60]
li=["helo","guys","iam","gayathri","lets","code","together"]
l=[0.2,0.5,7.8,9.3,45.6]
print(list)
print(li)
print(l)

#accessing list items note that lists are also 0 indexed like arrays
print(list[3])
print(li[-1]) # -1 refers to the last index
print(list[2:5])#last index is excluded
print(list[:5])
print(l[2:])

#changing list items
list[0]=0
print(list)
list[2:5]=[55,60 ,33,44]#i gave more values
print(list)
list[1:3]=[16]# i gave less values
print(list)

#adding elements to list
list.append(555)
print(list)

list.insert(2,777)
print(list)


list2=[888,999,444,666]
list.extend(list2)
print(list)


tuple1=(488,588,688,788)
list.extend(tuple1)
print(list)

#remove list items
l.remove(9.3)#if more than one item present remove removes first occurence
print(l)
list.pop(2)#removes specified index
print(list)
del list[0]#removes specified index and can also be used to del the entire list
print(list)
l.clear()
print(l)

