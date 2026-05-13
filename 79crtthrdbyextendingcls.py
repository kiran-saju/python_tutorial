#creating thread by extending thread class (object oriented way)

from threading import *
class My_Thread(Thread): 
    def run(self): #run() is a abstact method in Thread
        for i in range(10):
            print("python")
t=My_Thread()
t.start()
for j in range(10):
    print("Django")
