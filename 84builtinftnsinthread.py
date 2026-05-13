#1) is_alive() - checks whether a thread is running or not,returns a boolean value
'''
from threading import *
def display():
    print("Hello world")
def show():
    print("Python")

t1=Thread(target=display)
t2=Thread(target=show)
print("before running:",t1.is_alive())

t1.start()
print("after running:",t1.is_alive())
t2.start()
print("after running:",t2.is_alive())
'''
#2) active_count() - return no of running thread
'''
from threading import *
def display():
    print("Hello world")
    time.sleep(1)
def show():
    print("Python")
    time.sleep(1)
t1=Thread(target=display)
t2=Thread(target=show)

t1.start()
t2.start()

print("no.of threads:",active_count()) #o/p-3
'''

#3) enumerate()-returns list of all running threads
'''
from threading import *
import time
def display():
    print("Hello world")
    time.sleep(1)

def show():
    print("Python")
    time.sleep(1)

t1=Thread(target=display)
t2=Thread(target=show)

t1.start()
t2.start()

l=enumerate()
print(l)

'''

