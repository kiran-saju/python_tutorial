#function without arguments and with return value

#use keyword "return"

#1)
'''
def add():
    a=10
    b=5
    c=a+b
    return c
print("sum is",add())
'''
#or
'''
def add():
    a=10
    b=5
    c=a+b
    return c
k=add()
print("sum is",k)

'''


#difference between print() and return

#print() - built-in function
'''
def operation():
    a=10
    b=5
    c=a+b
    d=a-b
    print(c)
    print(d)
    print(c+50) #will work
operation()
# print(c+50)  #not work
'''
#or
'''
def operation():
    a=10
    b=5
    c=a+b
    d=a-b
    print(c)
    print(d)
k=operation()
print(k)
# print(k+50) #not work
'''

#return - keyword
'''
def operation():
    a=20
    b=5
    c=a+b
    d=a-b
    return c #once a return is used then stmnts after that "return" will not work 
    return d  #example
    print()   #example
k=operation()
print(k)
print(k+100)
'''
'''
def operation():
    a=20
    b=5
    c=a+b
    return c
k=operation()
print(k+100) #will work because return has only 1 value (c)
'''
'''
def operation():
    a=20
    b=5
    c=a+b
    d=a-b
    return c,d
k=operation()
print(k+100) #will work because return has 2 values (c and d)
'''

#2)
'''
def add():
    a=10
    b=20
    print(a+b)
add()
print(add()) #o/p will be none, because we didn't use return in the function. without return if we try to print a function then none is produced

'''

#with return
'''
def add():
    a=10
    b=20
    return a+b
print(add())
'''

#3) returning multiple values
''''
def operations():
    a=10
    b=5
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div
result=operations()
print(result)
print(type(result))
'''
