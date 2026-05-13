# immutable, ordered , heterogenous 

a=(1,2,'tiger','lion',3,4)
print(a)
print(len(a))
print(a[2])

#delete tuple
# del a
# print(a)

#immutable
'''
a[2]='ki'
print(a)
'''

print(type(a)) 

b=(3)
print(type(b)) #integer
b=(3,)
print(type(b)) #tuple

print(a.index(4))

#min,max
print(min(b))
print(max(b))

#count()
print(b.count(2)) #1

#nested tuple

a=(1,2,'tiger','lion',3,4,(1,2),(5,6,7))
#                         (0  1) (0 1 2)
#  0 1    2     3     4 5   6     7
print(type(a),a)
print(a[6][0]) #1
print(a[6][1]) #2
print(a[7][0]) #5
print(a[7][1]) #6
print(a[7][2]) #7
