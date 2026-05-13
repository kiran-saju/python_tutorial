#Basics
'''
class Human:
    def sleep(self):
        print("i can sleep")
    def work(self):
        print("I am a govt staff")
class Male(Human):
    def swim(self):
        print("I can swim")
    # def work(self):  #overiding problem
    #     print("I can code")
    def work(self):
        super().work() #solution to overriding
        print("I can code")
m1=Male()
m1.sleep() #inheriting
m1.work()  #inheriting #o/p-I am a govt staff
m1.swim()
# m1.work() #methdoverriding, o/p-I can code(not inherited)
m1.work() #solution to overriding

'''
'''
class Human:
    def __init__(self) :
        self.eyes=2
        self.nose=1
class Male(Human):
    def __init__(self,name):
        super().__init__()
        self.name=name
m1=Male("kiran")
print(m1.name)
print(m1.eyes)
print(m1.nose)
''' 
'''   
class Human:
    def __init__(self,heart) :
        self.eyes=2
        self.nose=1
        self.heart=heart
class Male(Human):
    def __init__(self,name,heart):
        super().__init__(heart)
        self.name=name
m1=Male("kiran",1)
print(m1.name)
print(m1.eyes)
print(m1.nose)   
print(m1.heart)   
''' 

'''
implement the concept of single inheritence using pyhon by create a base class named person with instance members name and age,usinga consructor initialize data memebrs
create a method display to show the details name and age,create a deried class named student from the base class person with instance memebrs rollno and location using a const to initialize data mem
include method overriding with the method named display to show details of instance members to cls stds
'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Person__init__")
    def display(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
class Student(Person):    
    def __init__(self,name,age,rollno,loc) :
            self.rollno=rollno
            self.loc=loc
            super().__init__(name,age) 
            print("student__init__")
    def display(self):
        super().display()
        print(f"rollno: {self.rollno}")
        print(f"loc: {self.loc}")
s1=Student("kiran",23,214,"anchal")
print(s1.name)
print(s1.age)
print(s1.rollno)
print(s1.loc)


#better example
class Father:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def hair(self):
        print('Black Hair')
    def eyes(self):
        print("Brown eyes")
    def height(self):
        print('6 feet')

class Son(Father):

    def __init__(self, firstname, father):  # Accept Father instance as argument
        super().__init__(firstname, father.lastname)  # Inherit last name from given Father instance
    def hair(self):
        super().hair()

    def eyes(self):
        super().eyes()

    def height(self):
        print("5.9 feet")
f1=Father("Alex","Garry")
s1=Son("John",f1)
s1.eyes()
s1.hair()
s1.height()



name=s1.firstname+s1.lastname
print("son name is",name)
        