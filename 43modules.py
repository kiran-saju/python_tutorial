'''
import math
print(math.sqrt(225))
a=print(math.sin(0))
'''
#also
'''
from math import sqrt
print(sqrt(100))
'''
#problem
'''
from math import sqrt
print(sqrt(100))
print(sin(0))
'''
#solution
'''
from math import sqrt,sin
print(sqrt(100))
print(sin(0))
'''

#import all functions in a module
'''
from math import *
print(sqrt(100))
#or
import math
print(math.sqrt(625))
print(math.cos(1))
'''

#import multiple modules
'''
import math,random
a=random.random()
print(a)
print(math.ceil(a))
'''

#module aliasing
'''
import math as m
a=m.sin(0)
print(a)

import random as r
a=r.random()
print(a)
'''