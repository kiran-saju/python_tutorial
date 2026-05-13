#types of variables

#1-instance variables/object level variables (contains self)
#2-static variables/class level variables
#3-local variables/method level variables 

#types of methods

#1-instance methods - connected to instance varible only (contains self) #most priority
#2-class methods - connected to class level/static variable
#3-static methods - connected to local variable #least priority

#type of variables example
'''
class Student:
    clgname="paranoia" #static variable
    def __init__(self,name,rollno):
        self.name=name  #instance variable
        self.rollno=rollno
    def sample(self):
        x=10 #instance variable
        for i in range(x):
            print(i)
'''
'''
class Student:
    clgname="MIIT" #class level/static variable
    HOD="Priji"  #class level/static variable
    
    def __init__(self,name,rollno): #instance method
        self.name=name #instance variable / object level variable
        self.rollno=rollno  #instance variable / object level variable
    
    def StudentInfo(self): #instance method
        print("Student name:",self.name)#instance variable
        print("Student rollno:",self.rollno)#instance variable

    @classmethod
    def ClgInfo(cls): #class method
        print("College:",cls.clgname) #class level variable
        print("HOD:",cls.HOD)

    @staticmethod
    def avgmark():
        a,b,c=10,20,30 #local variables
        print("average mark:",((a+b+c)/3))

s1=Student("kiran",23)
print(s1.name)

s1.StudentInfo()

Student.ClgInfo()
s1.ClgInfo()

Student.avgmark()
s1.avgmark()


'''
'''
class School:
    sname="SGCS"
    eyear=1995
    def __init__(self,name,rollno,age):
        self.name=name
        self.rollno=rollno
        self.age=age
    def StudentInfo(self):
        print(f"student name is { self.name}")
        print(f"student rollno is { self.rollno}")
        print(f"student age is { self.age}")
    @classmethod
    def SchoolInfo(cls):
        print(cls.sname)
        print(cls.eyear)
    @staticmethod
    def avgmark():
        a=100
        b=50
        c=70
        print((a+b+c)/3)
s1=School("kiran",23,23)
s1.StudentInfo()
School.SchoolInfo()
s1.avgmark()
'''
       
