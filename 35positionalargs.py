#positional arguments

#1)

#correct
'''
def details(name,age,course,place):
    print(f"Hi, my name is {name}. i'm {age}years old.i'm doing {course}. I'm comming from {place}")
details('kiran',23,'python','kollam')
'''
#incorect 
'''
def details(name,age,course,place):
    print(f"Hi, my name is {name}. i'm {age}years old.i'm doing {course}. I'm comming from {place}")
details('kiran','python',23,'kollam')
'''

#incorect 
'''
def details(name,age,course,place):
    print(f"Hi, my name is {name}. i'm {age}years old.i'm doing {course}. I'm comming from {place}")
details('kiran',23,'python','kollam','full stack')
'''

#2) find simple interest
'''
def cash(priciple_amount,rate,time):
    si=(priciple_amount*rate*time)/100
    return si
k=cash(10000,5,2)
print(k)

def amount():
    print(k+100)
amount()

'''

