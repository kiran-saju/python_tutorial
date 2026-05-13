#duck typing
'''
x=5
x="python"
print(x)
print(type(x))

x=5
y=10
print(x+y)

x="kiran"
y="anchal"
print(x+y)

x="python"
y=["lion","Tiger",1,2,3]
z=123
print(len(x))
print(len(y))
print(len(z))
'''

'''
class Duck:
    def quack(self):
        print("Quack!")

class Dog:
    def quack(self):
        print("Woof!")

def make_it_quack(thing):
    thing.quack()

duck = Duck()
dog = Dog()

make_it_quack(duck)  # Outputs: Quack!
make_it_quack(dog)   # Outputs: Woof!
'''

class employee1:
    def info(self):
        print("kiran")
        print("gowri")

class employee2:
    def info(self):
        print("Alpha")
        print("beta")
    def add(self):
        print("sum")
        
class department:
    def detail(self,emp):
        emp.info()

e1=employee1()
e2=employee2()
d1=department()
d1.detail(e1)
d1.detail(e2)