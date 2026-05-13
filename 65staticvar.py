#declaring static/class level variable
#1
'''
class Test:
    #1) within a class
    a=10
print(Test.__dict__)
'''
#2
'''
class Test:
    a=5
    #2) within a constructor
    def __init__(self):
        Test.b=10
t1=Test()
print(Test.__dict__)
'''
#3
'''
class Test:
    a=5
    def __init__(self):
        Test.b=10
    #3)inside a instance method
    def Sample(self):
        Test.c=15
t1=Test()
t1.Sample()
print(Test.__dict__)
'''
#4 within a class method
'''
class Test:
    a=5
    def __init__(self):
        Test.b=10
    def Sample(self):
        Test.c=15
    #4)inside a clas method
    @classmethod
    def sample2(cls):
        Test.d=20 #class var 
        cls.e=25 #class var 
t1=Test()
t1.Sample()
Test.sample2()
print(Test.__dict__)
'''
#5
'''
class Test:
    a=5
    def __init__(self):
        Test.b=10
    def Sample(self):
        Test.c=15
    @classmethod
    def sample2(cls):
        Test.d=20 #class var 
        cls.e=25 #class var 
    #5)inside a static method
    @staticmethod
    def demo():
        Test.f=30
t1=Test()
t1.Sample()
Test.sample2()
t1.demo()
print(Test.__dict__)
'''

#Access static variable
class Test:
    a=5
    #1 inside constructor
    def __init__(self):
        print(self.a)
        print(Test.a)
        
    #2) inside a instance metho
    def Sample(self):
        print("A - inside instance method :",self.a)
    
    #3) Inside class method
    @classmethod
    def sample1(cls):
        print("A:using cls",cls.a) #using cls
        print("A:using class name",Test.a)#using class name

    #4)inside static method
    @staticmethod
    def sample2():
        print("A:Using static method",Test.a)
        

t1=Test()
# print(Test.__dict__)

t1.Sample()
# print(Test.__dict__)

Test.sample1()
# print(Test.__dict__)

Test.sample2()
# print(Test.__dict__)
