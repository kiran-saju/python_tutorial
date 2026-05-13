#1)various places to declare instance variable
'''
#1)various places to declare instance variable


class Test:
    #1)inside class
    def __init__(self):
        self.a=5
        self.b=10

    def sample(self):
        self.c=15
        print(self.c)

    @staticmethod
    def local():
        d=4
        print(d)

s1=Test()
s1.sample()
print(s1.a)
print(s1.b)
s1.local()

#instance variables of a particular object
print(s1.__dict__)#d is not shown becz it's not instance variable

t2=Test()
t2.sample()
print(t2.__dict__)

#2)outside class
t2.d=50
t2.e=100
print(t2.__dict__)

#3)outside cls by object reference variable
t3=Test()
print(t3.__dict__)

'''
#2)accessing instance variable

'''
class Test:
    def __init__(self):
        self.a=5
        self.b=10
    #1)with in class using self
    def display(self):
        print(self.a)
        print(self.b)
s1=Test()
s1.display()
#outside class using object reference variable
print(s1.a) #here s1 is reference variable

'''
#3)update a instance variable
'''
class Test:
    def __init__(self) :
        self.a=5
        self.b=10
    #update inside a method
    def update(self):
        self.a=15
s1=Test()
s1.update()
print(s1.__dict__)

#update outside class
s1.a=100
print(s1.__dict__)

t2=Test()
print(t2.__dict__)
t2.a=100
print(t2.__dict__)
        
'''
#4)delete a instance variable
class Test:
    def __init__(self) :
        self.a=5
        self.b=10
        self.c=15
    #delete inside a method/class
    def remove(self):
        del self.b
t2=Test()
print(t2.__dict__)
t2.remove()
print(t2.__dict__)

 #delete outside a class
del t2.c
print(t2.__dict__)


