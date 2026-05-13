#public
'''
class Demo:
    def __init__(self):
        self.a=10 #public
    def display(self):
        print(self.a)
d1=Demo()
d1.display()
print("----")
d1.a=20 #modifying
d1.display()
'''

#private(__)
'''
class Demo:
    def __init__(self):
        self.__a=10
        print(id(self.__a))
    def __display(self):
        print(self.__a)
    def show(self):
        self.__display()
d1=Demo()
d1.show()
d1.__a=15 #tries to  modify
print(d1.__a) #modification unsuccessfull
print(id(d1.__a)) #stores in different m/y loc
'''
#name mangling (security issue)
'''
class Demo:
    def __init__(self):
        self.__a=10
        print(id(self.__a))
    def display(self):
        print(self.__a) 
d1=Demo()
print(d1.__dict__)
d1._Demo__a=15
print(d1.__dict__)
'''
#getter & setter (security issue)
'''
class Employee:
    def __init__(self):
        self.__salary=3000
    def get_salary(self): #for accessing
        print(self.__salary)
    def set_salary(self,salary):#modify
        self.__salary=salary #override
e1=Employee()
e1.get_salary()
e1.set_salary("4000")
e1.get_salary()

'''
# class SalaryDetails:
#     def __init__(self):
#         self.__salary=10000
#     def get_salary(self):
#         print(self.__salary)
#     def set_salary(self,salary):
#         self.__salary=salary #override
        
# s1=SalaryDetails()
# s1.get_salary()
# s1.set_salary(200)
# s1.get_salary()

class SalaryDetails:
    def __init__(self):
        self.__salary=10000
    def display(self):
        print(self.__salary)
       
s1=SalaryDetails()
print(s1.__dict__)
s1._SalaryDetails__salary=200
s1.display()
