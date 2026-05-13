#1) area of rectangle with all ftn variations

#ftn without args and without return value
def area1():
    l=int(input("enter length "))
    b=int(input("enter length "))
    print(l*b)
area1()

#ftn with args and without return value
def area2(l,b):
    print(l*b)
l=int(input("enter length "))
b=int(input("enter length "))  
area2(l,b)

#ftn without args and with return value
def area1():
    l=int(input("enter length "))
    b=int(input("enter length "))
    return l*b
k=area1()
print(k)


#ftn with args and with return value
def area1(l,b):
    l=int(input("enter length "))
    b=int(input("enter length "))
    return l*b
k=area1(l,b)
print(k)