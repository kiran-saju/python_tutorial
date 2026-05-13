#creating thread without extending thread class
from threading import*
class SampThread:
    def m1(self):
        for i in range(10):
            print("Hello")
obj=SampThread()
t=Thread(target=obj.m1) #thread creation
t.start() #thread invoking
for i in range(10):
    print("hai")
