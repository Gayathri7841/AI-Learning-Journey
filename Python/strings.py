sample="hello coders Gayathri here!"
print(sample)
print(type(sample))

sample1='hello world'
print(sample1)
print(type(sample1))

#quotes inside quotes
str="it's ok not to be ok"
print(str)
str='it"s ok not to be ok'
print(str)

#multiline string(line breaks wil be inserted as in the code)
str="""
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print(str)
str='''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
print(str)

#accessing string characters as strings are array of characters even 1 char is considered as string
str="gayathri"
print(str[5])

for x in "gayathri":
    print(x)

#method 1----------> length
str="hello guysssssssssssssssssssssssssssssss"
print(len(str))
#method2----------->in
str="The best things in life are free!"
text="free"
print(text in str)
#method2---------->not
str="The best things in life are free!"
text="free"
print(text not in str)

#strings slicing
x="Learning Python"
print(x[2:5]) # notice that character at index 5 is not included 

print(x[:5])

print(x[2:])

print(x[-5:-2])

#python in built methods to modify strings
#method 1----------> length
str="hello guysssssssssssssssssssssssssssssss"
print(len(str))
#method2 ----------->upper()
print(str.upper())
#method3 ----------->lower()
print(str.lower())
#method4------------->strip()
str="   hello world    "
print(str.strip())
#method5------------->replace()
print(str.replace("h","j"))
#method6-------------->split()
s="hello,my,name,is,gayathri"
print(s.split(","))

#String formatting
price=70
text=f"the price is {price} dollars"
print(text)












