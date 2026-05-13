from random import random
#range btwn 0-1
print(random())


#randrange() - predefined random range
from random import randrange
a=randrange(1,11) #print start value,but not end value
print(a)

b=randrange(2,10,2)#step value can also be included
print(b)


#randint() - numbers btwn 2 nums which prints start and end nums also 
from random import randint
c=randint(1,10)  
print(c)

d=randint(8,12)
print(d)

#uniform() - get float value as output
from random import uniform
d=uniform(0,1)
print(d)
d=uniform(1,5)
print(d)
e=uniform(8,12)
print(e)


#choice - don't work in set and dict
from random import choice
l1=[11,22,33,44,55]
e=choice(l1)
print(e)

t1=(11,22,33,44,55)
e=choice(t1)
print(e)



#shuffle() - works only on list

from random import shuffle
mylist = ["apple", "banana", "cherry"]
print(mylist)
shuffle(mylist) #can't store this to a variable
print(mylist)
