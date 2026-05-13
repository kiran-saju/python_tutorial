#lock
'''
from threading import *

lock=Lock()

def task(lock,msg):
    lock.acquire()
    for i in range(1,6): 
        print(msg)
    lock.release()
b1=Thread(target=task,args=(lock,"Hello world",))
b2=Thread(target=task,args=(lock,"welcome",))

b1.start()
b2.start() 
'''
'''
#Rlock(re enterent lock)
from threading import *
# lock=Lock()
lock=RLock()
def even():
    lock.acquire()
    for i in range(2,10,2):
        print(i,current_thread().name)
    lock.release()
def odd():
    lock.acquire()
    for i in range(1,9,2):
        print(i,current_thread().name)
    lock.release()
def oddEven():
    # lock.acquire() makes pgm crash
    even() 
    odd()
    # lock.release()
b1=Thread(target=oddEven)
b2=Thread(target=oddEven)
# b3=Thread(target=oddEven)

b1.start()
b2.start() 
# b3.start()
'''
'''
#eg1
from threading import *
lock=RLock()
class Bus:
    def __init__(self,name,av_seat,lock):
        self.name=name
        self.av_seat=av_seat
        self.lock=lock

    def reserve(self,seat_needed):
        self.lock.acquire()
        print("Available seats:",self.av_seat)
        if self.av_seat>=seat_needed:
            name=current_thread().name
            print(f"{seat_needed} allocated to {name}")
            self.av_seat-=seat_needed
        else:
            print("no seat avalilable")
        self.lock.release()
        
b1=Bus("Python travels",2,lock)
t1=Thread(target=b1.reserve,args=(2,),name="abc")
t2=Thread(target=b1.reserve,args=(2,),name="xyz")

t1.start()
t2.start()

'''

#3) Semaphore
'''
from threading import *
from time import *

s=Semaphore()
def display(name):
    s.acquire()
    for i in range(1,4):
        print("python",name)
        sleep(2)
    s.release()
t1=Thread(target=display,args=("T-1",))
t2=Thread(target=display,args=("T-2",))
t3=Thread(target=display,args=("T-3",))
t4=Thread(target=display,args=("T-4",))
t5=Thread(target=display,args=("T-5",))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

'''

