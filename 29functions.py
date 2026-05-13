#1)built-in functions
# print(),len(),sum()

#2) function defined in a module
'''
import math
a=math.sqrt(100)
print(a)
'''

#3) user defined function
'''
def greet():                   #declaration
    print("good morning")       #block of code
greet()                        #function call
'''

'''
def greet():    
    name=input("enter name ")               
    print("good morning " + name)       
greet() 

'''

'''
def sum():
    numbr1=int(input("enter first number "))
    numbr2=int(input("enter second number "))
    print("sum is",numbr1+numbr2)
sum()
'''