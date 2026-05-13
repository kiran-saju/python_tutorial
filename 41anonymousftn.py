
#1) square of a num
#normal function
def sqaure(a):
    return a**a
k=sqaure(5)
print(k)

#anonymous function 
x= lambda a: a**a
print(x(5))

#2) sum of 2 nums
x= lambda a,b: a+b
print(x(5,4))

#3) diff of 3 nums
y=lambda a,b:a-b
print(y(1,2))
