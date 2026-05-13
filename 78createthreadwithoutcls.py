#creating thread without using class(functional oriented)
'''
from threading import*
def display():
    for i in range(10):
        print(" child thread ")
t=Thread(target=display)#thread creation (Thread is the inbuilt Class)
t.start() #child thread invoked by mainthread
for j in range(10): 
    print(" Main thread ")
'''
'''
from threading import*
def display():
    for i in range(10):
        print(current_thread().getName())
t=Thread(target=display)#thread creation (Thread is the inbuilt Class)
t.start() #child thread invoked by mainthread
for j in range(10): 
    print(current_thread().getName())
'''

#eg1

#write a pgm to create  2 threads to find and print even and odd numbers (even nos=2To20,odd=30To50)

from threading import *

def even():
    for i in range(2,20,2):
        print("even nos are: ",i,current_thread().name)

t1=Thread(target=even)
t1.start()

def odd():
    for j in range(21,50,2):
        print("odd nos are: ",j,current_thread().name)
t2=Thread(target=odd)
t2.start()
