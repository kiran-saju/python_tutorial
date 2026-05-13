#eg1
'''
class Human: #parent class 1
    def sleep(self):
        print("i can sleep")
    def work(self):
        print("I am soldier")
class Male:  #parent class 2
    def beard(self):
        print("i have beard")
    def work(self):
        print("I am s/w dev")
class Boy(Human,Male): #child class
    def work(self):
        print("I am s/w tester")
    
b1=Boy()
b1.beard()
b1.sleep()
Human.work(b1)
print(Boy.mro()) #method resolution order
Male.work(b1)
b1.work()
'''
#or
'''
class Human: #parent class 1
    def sleep(self):
        print("i can sleep")
    def work(self):
        print("I am soldier")
class Male:  #parent class 2
    def beard(self):
        print("i have beard")
    def work(self):
        print("I am s/w dev")
class Boy(Human,Male): #child class
    def work(self):
        print("I am s/w tester")
        Male.work(self)
        Human.work(self)    
b1=Boy()
b1.beard()
b1.sleep()
b1.work()
'''
#eg2
'''
class Human:
    def __init__(self,heart):
        # print("human init")
        self.eyes=2
        self.nose=1
        self.heart=heart
class Male:
    def __init__(self,kidney):
        # print("male init")
        self.brain=1
        self.kidney=kidney
class Boy(Human,Male):
    def __init__(self,name,heart,kidney):
        Human.__init__(self,heart)
        Male.__init__(self,kidney)
        self.name=name
b2=Boy("kiran",1,2)
print(b2.name)
print(b2.eyes)
print(b2.nose)
print(b2.brain)
print(b2.heart)
print(b2.kidney)
'''
#eg3
class Human:
    def __init__(self,heart):
        self.heart=heart
        self.eyes=2
        self.nose=1
    def work(self):
        print("dotor")
class Male:
    def __init__(self,kidney):
        self.kidney=kidney
        self.brain=1
    def work(self):
        print("teacher")
class Boy(Human,Male):
    def __init__(self,name,heart,kidney):
        Human.__init__(self,heart)
        Male.__init__(self,kidney)
        self.name=name
    def work(self):
        print("police")
        Human.work(self)
        Male.work(self)

b1=Boy("kiran",1,2)
print("name:",b1.name)
print("heart:",b1.heart)
print("kidney:",b1.kidney)
print("brain:",b1.brain)
print("eyes:",b1.eyes)
print("nose:",b1.nose)
print("works are:")
b1.work()




    