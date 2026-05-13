'''

#inaccurate example 1
class TrainerDetails():

    #attributes(properties)
    def __init__(self) :#special method  
        self.name='kiran' 
        self.age=23
        self.qualification='MCA'

    #method(behaviour)
    def teach(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"qualification:{self.qualification}")
    
    def study(self):
        print("u r studying ")
    

#access attributes and behaviour
#object creation
t1=TrainerDetails() # t1 is reference variable

print(t1.name)
t1.teach()
t1.study()
'''

'''
#inaccurate example 2
class Student(): #class
    pass

s1=Student() #object
s1.name="kiran" #property of object s1
s1.rollno= 1  #property of object s1
print(s1.name,s1.rollno)
print(type(s1))

s2=Student()
s2.name="virat" #property of object s2
s2.rollno=2     #property of object s2
print(s2.name,s2.rollno)

'''
'''
#inaccurate example 3
class Student(): #class
    def __init__(self) : #special method or in general called constructor
        self.name="kiran" #property
        self.age=23       #property
        self.rollno=700   #property
s1=Student() #object
print(s1.name)
s2=Student() #object
print(s2.name)

#s1&s2 saves in different m/y loc
print(id(s1))
print(id(s2))
'''
'''
#checks __init__ is calling or not
class Student(): #class
    def __init__(self) : #special method or in general called constructor
        print("constructor called, object created ")

s1=Student() #object

s2=Student()

'''
'''
#accurate example1, class is now dynamic
class Student:
    #attributes or property creation
    def __init__(self,name,age,rollno) :
        print("constructor called, object created ")
        self.name=name #propery
        self.age=age   #propery
        self.rollno=rollno #propery

    #method or beahviour creation
    def study(self):
        print("I can Learn")
    def extra(self):
        print("I love sports")

#object creation
s1=Student("virat",30,18)
print(s1.name)
print(s1.age)
print(s1.rollno)
#object creation
s2=Student("messi",30,8)

#accessing attributes
print(s2.name)
print(s2.age)
print(s2.rollno)

#accessing methods
s1.study()
s2.extra()

#modifying attribues
s1.name="kiran"
print(s1.name)
'''


'''
#accurate example2
class Student:
    def __init__(self,name,age,rollno):
        #init is used to give attributes to objects
        #self is a reference variable used inside class
        print(id(self))
        self.name=name
        self.age=age
        self.rollno=rollno
    def show(self):
        print(f"Name:{self.name}")
        print(f"age:{self.age}")
        print(f"rollno:{self.rollno}")
        print(id(self)) #same as s1
#object creation
s1=Student("virat",30,18)
#s1 is a reference variable used outside class
print(s1.name)
print(s1.age)
print(s1.rollno)
print(id(s1)) #same as self
#methodaccess
s1.show()

'''

#args in class
''''
class Teacher():
    def teach(self,*args):
        for arg in args:
            print(arg)

t1=Teacher()
t1.teach("kiran","anu","gopu")
'''

#kwargs in class
''''
class Teacher():
    def subjects(self,**kwargs):
        for key,value in kwargs.items():
            print(f"{key} : {value}")
t2=Teacher()
t2.subjects(name='kiran',sub='python')
'''