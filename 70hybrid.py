# class A:
#     def display(self):
#         print("Display From A")
# class B(A):
#     def display(self):
#         print("Display From B ")
# class C:
#     def display(self):
#         print("Display From C")
# class D(B,C):
#     def display(self):
#         print("Display from D")
        
#         C.display(self)
#         B.display(self)
# d1=D()
# d1.display()

class A:
    def __init__(self,eyes,nose):
        self.eyes=eyes 
        self.nose=nose
    def display(self):
        print("Display From A")
class B(A):
    def __init__(self,eyes,nose):
        self.kidney=2
        A.__init__(self,eyes,nose)
    def display(self):
        print("Display From B ")
class C:
    def __init__(self,heart):
        self.heart=heart 
    def display(self):
        print("Display From C")
class D(B,C):
    def __init__(self,heart,eyes,nose):
        B.__init__(self,eyes,nose)
        C.__init__(self,heart)
    def display(self):
        print("Display from D")
        print("kidney:",self.kidney) 
       
d1=D(1,2,1)
A.display(d1)
B.display(d1)
C.display(d1)
D.display(d1)
print()
print("no of nose:",d1.nose)
print("no of eyes:",d1.eyes)
print("no of heart:",d1.heart)
print("no of kidney:",d1.kidney)


        
        