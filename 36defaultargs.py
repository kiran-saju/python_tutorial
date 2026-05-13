#default arguments

#1)
'''
def details(name,age,course,place='tvm'):
    print(f"name is {name}.age is {age}. course is {course}.place is {place}")
details('virat',25,'java')
'''

#overwrite
'''
def details(name,age,course,place='tvm'):
    print(f"name is {name}.age is {age}. course is {course}.place is {place}")
details('virat',25,'java',"kollam")
'''

#2) default args can only be passed as last parameters
'''
def details(name,age,course='java',place):
    print(f"name is {name}.age is {age}. course is {course}.place is {place}")
details('virat',25,'ekm')
'''
#but
'''
def details(name,age,course='java',place='ekm'):
    print(f"name is {name}.age is {age}. course is {course}.place is {place}")
details('virat',25)
'''

#2) find simple interest
'''
def cash(priciple_amount,rate,time=2):
    si=(priciple_amount*rate*time)/100
    return si
k=cash(10000,5)
print(k)
'''
