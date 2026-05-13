'''
class ArithmeticOperations:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def sum(self):
        c=self.num1+self.num2
        print("sum is", c)
    def diff(self):
        d=self.num1-self.num2
        print("diiference is ",d)
s1=ArithmeticOperations(20,10)
s1.sum()
s1.diff()

'''

'''
class circle:
    def __init__(self,pi,r):
        self.pi=pi
        self.r=r
    def circumference(self):
        c=2*self.pi*self.r
        print("circumference is", c)
    def area(self):
        d=self.pi*self.r**2
        print("area is ",d)
s1=circle(3.14,10)
s1.circumference()
s1.area()
'''
'''
class Triangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        a=1/2*(self.l*self.b)
        print("area is ",a)
s1=Triangle(2,2)
s1.area()
'''
'''
class Person:
    def __init__(self,name,age,mobile):
        self.name=name
        self.age=age 
        self.mobile=mobile
    def details(self):
        print(f"name is {self.name}")
        print(f"age is {self.age}")
        print(f"mobile is {self.mobile}")
s1=Person("kiran",23,67667887)
s1.details()
'''

'''
class Movie:
    def __init__(self,moviename,actor,genre):
        self.movie=moviename
        self.actor=actor
        self.genre=genre
    def details(self):
        print(f"movie name is {self.movie}")
        print(f"actor name is { self.actor}")
        print(f"genre is {self.genre}")
movie_list=[]
while True:
    moviename=input("enter movie name")
    actorname=input("enter actor name")
    genre=input("enter genre")
    m=Movie(moviename,actorname,genre)
    movie_list.append(m)
    print("details added successfully")
    choice=input("do u want to enter more movie details?y/n")
    if choice=="y":
        # break
        continue
    elif choice=="n":
        break
    else:
        print("invalid input")
# print(movie_list)
for i in movie_list:
    i.details()
    print()

'''


