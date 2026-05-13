#two types 
# 1) primitive and 2)non primitive
"""
Primitive- Primitive types store a single value 
and are the basic building blocks of programs.
"""
 #1)number
a=2
print(a)

#int

'''
a=int(input("1st num"))
b=int(input("2nd num"))
c=a+b
print(c)

'''

#float
'''
a=float(input("1st num"))
b=float(input("2nd num"))
c=a+b
print(c)

'''


#2)string
b="kiran"
print(b)

fname=input("enter first name")
lname=input(" enter second name")
name= fname +" "+ lname
print("name is ",name)

#3)boolean 
c=2
d=1
e=c>d
f=d>c
print(e)
print(f)

#4)complex
x=1.0
y=1.0
z=complex(x,y)
print(z)
#or
s=(1+2j)
print(s,type(s))

#Non primitive datatypes are - List,Dict,Tuple,Set
#Non-primitive types can store multiple values or more complex data structures.