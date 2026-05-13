#mean - (average)

from statistics import mean
l1=[1,4,6,11,44]
print(mean(l1))


#median - center element from element

from statistics import median
l1=[1,4,6,11,44]
print(median(l1))

l1=[10,20,30,40] #sum of middle nums / 2
print(median(l1))

#mode - most repeated number
from statistics import mode
l1=[11,30,30,40,50] 
print(mode(l1))

l1=[11,20,11,30,30,40,50]  #first most repeated num is printed(here 11)
print(mode(l1))

l1=[11,11,30,30,30,40,50]  
print(mode(l1))

l1=[11,30,40,50]  #no repeatition then first number is printed
print(mode(l1)) 
