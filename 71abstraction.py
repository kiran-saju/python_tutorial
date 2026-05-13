# Abstract class and abstract method
'''
from abc import ABC,abstractmethod
class Bmw(ABC): #abstract class
    def __init__(self,model,color):
        self.model=model
        self.color=color
    def use(self):
        print("For Travelling")
    @abstractmethod
    def Engine(self): #abstract method
        pass
class Bmwpet1(Bmw): #concrete class
    def __init__(self,series,model,color):
        Bmw.__init__(self,model,color)
        self.series=series
    def roof(self):
        print("open roof")
    def Engine(self):
        print("petrol engine")
p1=Bmwpet1('x',2023,'red')
p1.Engine()
p1.use()
class Bmwpet2(Bmwpet1):
    def __init__(self,series,model,color):
        Bmw.__init__(self,model,color)
        self.series=series
    def roof(self):
        print("open roof")
    def Engine(self):
        print("diesel engine")
p2=Bmwpet2('x',2023,'red')
p2.Engine()
p2.use()
'''

#2)
'''
create an abstract cls animls with 2 abst methods cats and dogs.
now create a cls cat with a method cat which prints cats sounds like mewo and cls dogs with method dog which prints bow bow
both inheriting the cls animals.now create an object for the sub clses and call respective objects.
'''
'''
from abc import ABC,abstractmethod
class Animals(ABC):
    @abstractmethod
    def sound(self):
        pass
class Cat(Animals):
    def sound(self):
        print("Meow")
class Dog(Animals):
    def sound(self):
        print("bow bow")
a1=Cat()
a1.sound()
a2=Dog()
a2.sound()
'''

from abc import ABC,abstractmethod
class BMW(ABC):
    def __init__(self,model,color):
        self.model=model
        self.color=color
    def purpose(self):
        print("travelling")
    @abstractmethod
    def Engine(self):
        pass
# b1=BMW(2023,'black')
class bmwp(BMW):
    def roof(self):
        print("sun roof")
    def Engine(self):
        print("petrol engine")
class bmwh(BMW):
    def roof(self):
        print("open roof")
    def Engine(self):
        print("hybrid engine")
b1=bmwp(2023,'black')
b1.Engine()
b1.purpose()
print()
b2=bmwh(2021,'red')
b2.Engine()
b2.purpose()

