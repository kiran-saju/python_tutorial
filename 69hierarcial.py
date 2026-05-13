#using method only

#1st method
'''
class Human:
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I am a Designer")
class Male(Human):
    def write(self):
        print("I can write")
    def work(self):
        print("I am a Developer")
        super().work()
class Female(Human):
    def run(self):
        print("I can read")
    def work(self):
        print("I am a Tester")
        
m1=Male()
m1.sleep()
m1.write()
m1.work()
print()
# f1=Female()
# f1.sleep()
# f1.run()
# f1.work()

'''
#2nd method
'''
class Human:
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I am a Designer")
class Male(Human):
    def write(self):
        print("I can write")
    def work(self):
        print("I am a Developer")
class Female(Human):
    def run(self):
        print("I can read")
    def work(self):
        print("I am a Tester")
        
m1=Male()
m1.sleep()
m1.write()
m1.work()
Human.work(m1)
print()
# f1=Female()
# f1.sleep()
# f1.run()
# f1.work()
'''

#3rd method
'''
class Human:
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I am a Designer")
class Male(Human):
    def write(self):
        print("I can write")
    def work(self):
        print("I am a Developer")
        Human.work(self)
class Female(Human):
    def run(self):
        print("I can read")
    def work(self):
        print("I am a Tester")
        Human.work(self)    
m1=Male()
m1.sleep()
m1.write()
m1.work()
print()
f1=Female()
f1.sleep()
f1.run()
f1.work()
'''

#using attributes only
'''
class Human:
    def __init__(self,heart):
        self.eyes=2
        self.nose=1
        self.heart=heart
class Male(Human):
    def __init__(self,numheart,kidney):
        Human.__init__(self,numheart)
        self.kidney=kidney
class Female(Human):
    def __init__(self,heart,hair):
        Human.__init__(self,heart)
        self.hair=hair

m1=Male(1,2)
print(m1.heart)
print(m1.eyes)
print(m1.nose)
print(m1.kidney)

'''

'''
create a cls named member it should ctn instance variable name,age,phnno,address,salary. 
it also has a method named printsalary which prints salary
 of memeber and printInfo() which prints details of member except salary.
2 clses, employee and manager inherits the member cls.
 the employee and manager clses have data members or instance var date of joining and dept.
also it have method printDateofJOining and printDept.
now assign name age adres salary phno to an employee and manager making an objet of both of this clses and print all details
'''
class Member:
    def __init__(self,name,age,phno,address,salary):
        self.name=name
        self.age=age
        self.phno=phno
        self.address=address
        self.salary=salary
    def printSalary(self):
        print(f"salary is:{self.salary}")
    def printInfo(self):
        print(f"name is:{self.name}")
        print(f"age is:{self.age}")
        print(f"phno is:{self.phno}")
        print(f"salary is:{self.address}")
    
class Employee(Member):
    def __init__(self,salary,name,age,address,phno):
        self.joindate="4-may-2022"
        self.dept="accountancy"
        Member.__init__(self,salary,name,age,address,phno)
    def printJoinDate(self):
        print(f"join date:{self.joindate}")
        print(f"Dept:{self.dept}")
        
class Manager(Member):
    def __init__(self,salary,name,age,address,phno):
        self.joindate="jan-2-2012"
        self.dept="Sales"
        Member.__init__(self,salary,name,age,address,phno)
    def printJoinDate(self):
        print(f"join date:{self.joindate}")
        print(f"Dept:{self.dept}")

e1=Employee("kiran",2000,23,"hgjh",54566)
e1.printInfo()
e1.printJoinDate()
print(e1.name)
print(e1.salary)
print(e1.age)
print(e1.address)
print(e1.dept)
print("join date:",e1.joindate)
print()
m1=Manager("kiran",2000,23,"hgjh",54566)
m1.printInfo()
m1.printJoinDate()