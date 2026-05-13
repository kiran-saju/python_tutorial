#ZeroDivisionError: division by zero
'''
n1=int(input("enter a number"))
n2=int(input("enter a number"))
res=n1/n2 #if n2=0
print(res)
print("thank you")
'''

#try block
'''
n1=int(input("enter a number"))
n2=int(input("enter a number"))
try:
    res=n1/n2 
    print(res)
    print("thank you")
except ZeroDivisionError:
    print("Try again") 
'''

#ValueError
'''
try:
    n1=int(input("enter a number"))
    n2=int(input("enter a number"))
    res=n1+n2
    print(res)
    print("thank you")
except ValueError:
    print("enter a integer value")

'''

#without specifying particular exception error
'''
try:
    n1=int(input("enter a number"))
    n2=int(input("enter a number"))
    res=n1/n2 
    print(res)
    print("thank you")   
except :
    print("Try again") 
'''
#try-except-else
'''

try:
    n1=int(input("enter a number"))
    n2=int(input("enter a number"))
    res=n1/n2 
    print("division successfully done")   
except :
    print("Try again") 
else:
    print(res)
finally:
    print("thank you")

'''
