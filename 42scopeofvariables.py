'''
a=10 #global variable
def check():
    a=15 ##local variable
    print("inside",a)
check()
print("outside",a)
'''

a=10 #global variable
def check():
    global a 
    a=15
    print("inside",a)
check()
print("outside",a)

def check1():
    return a+30
k=check1()
print(k)