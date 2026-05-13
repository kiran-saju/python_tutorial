# Arbitary or variable length

#Type2-> Arbitary keyword arguments

#problem
'''
def details(name,age,course,place):
    print(f"name is {name}, age is {age}, course is {course}, place is {place}")
details('kiran','23','python','klm')
details('kiran','python','tvm')

'''
#solution
def details(**kwargs):
    print(f"name is {kwargs.get('name')}, age is {kwargs.get('age')}, course is {kwargs.get('course')}, place is {kwargs.get('place')}")

details(name='kiran', age='23', course='python', place='klm')

'''
def details(**kwargs):
    for i in kwargs:
        print(i,kwargs[i])
        print(type(kwargs))
details(name='kiran',age=23,course='python',place='klm')
details(name='kiran',course='python',place='klm')

'''
def details(**data):
    for i in data:
        print(i,data[i])
details(age=23,name='kiran')

