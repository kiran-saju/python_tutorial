t=(6,1,2,3,4,5,5,5)
print(t)
print(type(t))
print(t.index(4))
print(t.count(5))
print(sorted(t)) #output will be in list

l=list(t)
print(l)
print(type(l))
l.append(500)
l[1]=200
t=tuple(l)
print(t)
print(type(t))


x=(8,2,1,9,0,10)
# y=sorted(x)
# print(y)
print(sorted(x))
# z=sorted(x,reverse=True)
print(sorted(x,reverse=True))


print(sum(x))
print(max(x))
print(min(x))