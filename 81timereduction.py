#Time delay
'''
import time
def doubles(numbers):
    for i in numbers:
        time.sleep(1)
        print("double : ",2*i)
def sqaures(numbers):
    for i in numbers:
        time.sleep(1)
        print("squares :", i*i)
numbers=[1,2,3,4,5,6]
begin_time=time.time()
doubles(numbers)
sqaures(numbers)
end_time=time.time()
total_time=end_time-begin_time
print("total time :",total_time)

'''

#using threading for reduce time delay 
''''
import time
from threading import *
def doubles(numbers):
    for i in numbers:
        time.sleep(1)
        print("double : ",2*i)
def sqaures(numbers):
    for i in numbers:
        time.sleep(1)
        print("squares :", i*i)
numbers=[1,2,3,4,5,6]
begin_time=time.time()

t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=sqaures,args=(numbers,))

t1.start()
t2.start()

t1.join() #to make wait main thread
t2.join()

end_time=time.time()

total_time=end_time-begin_time
print(total_time)

'''

