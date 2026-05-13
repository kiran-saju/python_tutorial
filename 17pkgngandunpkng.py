#updaing value of an item in tuple
#1
a=(1,2,3,'tiger','lion')
print(a)
#packing
i,j,x,y,z=a
print(type(i),i)
print(j)
print(x)
print(y)
print(z)
i=100 #value updated
#unpacking
a=i,j,x,y,z
print(a)


#2
x=(3.5,'virat','messi','cricket','football')
print(x)
i,j,k,l,m=x
j='rohit'
k='ronaldo'
x=i,j,k,l,m
print(x)



