#filter() - takes 2 arguments.1st one is logic(function) and 2nd one is iterable
list1=[1,2,4,3,8,24,62]
even_nums= list(filter(lambda n:n%2==0,list1))
print(even_nums)

#map() - takes 2 arguemts.1st one is logic(function) and 2nd one is iterable
doubles=list(map(lambda n:n*2,even_nums))
print(doubles)

#reduce()- takes 2 argu,emts.1st one is logic(function) and 2nd one is iterable
from functools import reduce
sum= reduce(lambda a,b:a+b,doubles)
print(sum)