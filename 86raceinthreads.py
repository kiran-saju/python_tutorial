#eg1

'''
from threading import *
lock=Lock()
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

#eg2
'''
from threading import *
lock=Lock()
def nums():
    # lock.acquire() if use 2 acquire() pgm will crash
    lock.acquire()
    for i in range(0,10,2):
        print(i,current_thread().name)
    lock.release()
    # lock.release()
t1=Thread(target=nums)
t2=Thread(target=nums)

t2.start()
t1.start()
'''
