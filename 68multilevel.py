#eg1
'''
class Human:
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I am designer")
class Male(Human):
    def beard(self):
        print("I have beard")
    def work(self):
        print("I am dev")
class Boy(Male):
    def work(self):
        print("I am a tester")
        Human.work(self)
        Male.work(self)
b1=Boy()
# b1.sleep()
# b1.beard()
# Male.work(b1)
# Human.work(b1)
b1.work()
print(Boy.mro())
'''
#eg2
'''
class Human:
    def __init__(self,Heart):
        self.eyes=2
        self.nose=1
        self.Heart=Heart
class Male(Human):
    def __init__(self,kidney,Heart):
        Human.__init__(self,Heart)
        self.brain=1
        self.kidney=kidney
class Boy(Male):
    def __init__(self,name,Heart,kidney):  
        Male.__init__(self,kidney,Heart)
        self.name=name
b2=Boy("kiran",1,2)
print(b2.name)
print(b2.eyes)
print(b2.nose)
print(b2.brain)
print(b2.Heart)
print(b2.kidney)
'''
#eg3
'''
class Human:
    def __init__(self,heart):
        self.eyes=2
        self.nose=1
        self.heart=heart
    def work(self):
        print("I am a designer")
class Male(Human):
    def __init__(self,heart,kidney):
        Human.__init__(self,heart)
        self.brain=1
        self.kidney=kidney 
    def work(self):
        print("I am Dev")
class Boy(Male):
    def __init__(self,name,kidney,heart):
        Male.__init__(self,kidney,heart)
        self.name=name
    def work(self):
        print("I am a tester")
b2=Boy("kiran",1,2)
print(b2.name)
print(b2.eyes)
print(b2.nose)
print(b2.brain)
print(b2.heart)
print(b2.kidney)
Human.work(b2)
Male.work(b2)
Boy.work(b2)
'''




class Apoopan:
    def __init__(self):
        self.wealth="1 acre"

class Achan(Apoopan):
    def __init__(self):
        Apoopan.__init__(self)
    
class Me(Achan):
    def __init__(self):
        Achan.__init__(self)
     
m1=Me()
print(m1.wealth)

        


    

        