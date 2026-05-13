#operator overloading
'''
x=5
y=10
print(int.__add__(x,y))
'''

#eg
'''
class SalaryDetails:
    def __init__(self,salary):
        self.salary=salary
    def __add__(self,x):
        return self.salary+x.salary
s1=SalaryDetails(10000)
s2=SalaryDetails(5000)
print(s1+s2)
# print(type(s1))

class SalaryDetails:
    def __init__(self,salary):
        self.salary=salary
    def __sub__(self,x):
        return self.salary-x.salary
s1=SalaryDetails(10000)
s2=SalaryDetails(5000)
print(s1-s2)
# print(type(s1))

class SalaryDetails:
    def __init__(self,salary):
        self.salary=salary
    def __truediv__(self,x):
        return self.salary/x.salary
s1=SalaryDetails(1000)
s2=SalaryDetails(5000)
print(s1/s2)


class SalaryDetails:
    def __init__(self,salary):
        self.salary=salary
    def __mul__(self,x):
        return self.salary*x.salary
s1=SalaryDetails(1000)
s2=SalaryDetails(5000)
print(s1*s2)
'''