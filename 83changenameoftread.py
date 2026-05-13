#type1 (older version)
'''
from threading import *
def display():
    print(current_thread().setName("samp1"))
    print(current_thread().name)
    for i in range(1,6):
        print("Hello world")
def show():
    print(current_thread().setName("samp2"))
    print(current_thread().name)
    for i in range(1,6):
        print("Python")
t1=Thread(target=display)
t2=Thread(target=show)

t1.start()
t2.start()
'''

#type2
'''


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

t1.name="samp1"
print(t1.name)
t2.name="samp2"
print(t2.name)

'''
'''
from threading import *
def display():
    for i in range(1,6):
        print("Hello world")
def show():
    for i in range(1,6):
        print("Python")
t1=Thread(target=display,name="Samp1")
t2=Thread(target=show,name="samp2")

t1.start()
t2.start()

print(t1.name)
print(t2.name)
'''

#id of thread
'''
from threading import *
def display():
    for i in range(1,6):
        print("Hello world")
def show():
    for i in range(1,6):
        print("Python")
t1=Thread(target=display,name="Samp1")
t2=Thread(target=show,name="samp2")

t1.start()
t2.start()

print(t1.ident)
print(t2.ident)
'''
#eg write a pgm to create multiple threads and print their names and also re assign their names

from threading import *
def display():
    print(current_thread().name)
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

t1.name="samp1"
print(t1.name)
t2.name="samp2"
print(t2.name)