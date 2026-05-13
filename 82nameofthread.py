#type1
'''
from threading import *
def display():
    print(current_thread().name) #name is a property
    for i in range(1,6):
        print("Hello world")
def show():
    print(current_thread().name)
    for i in range(1,6):
        print("Python")
t1=Thread(target=display)
t2=Thread(target=show)

t1.start()
t2.start()
'''

#type2 (used in older version)
'''
from threading import *
def display():
    print(current_thread().getName()) #name is a propert
    for i in range(1,6):
        print("Hello world")
def show():
    print(current_thread().getName())
    for i in range(1,6):
        print("Python")
t1=Thread(target=display)
t2=Thread(target=show)

t1.start()
t2.start()

'''

#type 3

from threading import *
def display():
    for i in range(1,6):
        print("Hello world")
def show():
    for i in range(1,6):
        print("Python")
t1=Thread(target=display)
t2=Thread(target=show)

t1.start()
t2.start()

print(t1.name)
print(t2.name)